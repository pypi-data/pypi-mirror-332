<a href="https://explosion.ai"><img src="https://explosion.ai/assets/img/logo.svg" width="125" height="125" align="right" /></a>

# spaCy Layout: Process PDFs, Word documents and more with spaCy

This plugin integrates with [Docling](https://ds4sd.github.io/docling/) to bring structured processing of **PDFs**, **Word documents** and other input formats to your [spaCy](https://spacy.io) pipeline. It outputs clean, **structured data** in a text-based format and creates spaCy's familiar [`Doc`](https://spacy.io/api/doc) objects that let you access labelled text spans like sections or headings, and tables with their data converted to a `pandas.DataFrame`.

This workflow makes it easy to apply powerful **NLP techniques** to your documents, including linguistic analysis, named entity recognition, text classification and more. It's also great for implementing **chunking for RAG** pipelines.

> 📖 **Blog post:** ["From PDFs to AI-ready structured data: a deep dive"
](https://explosion.ai/blog/pdfs-nlp-structured-data) – A new modular workflow for converting PDFs and similar documents to structured data, featuring `spacy-layout` and Docling.

[![Test](https://github.com/explosion/spacy-layout/actions/workflows/test.yml/badge.svg)](https://github.com/explosion/spacy-layout/actions/workflows/test.yml)
[![Current Release Version](https://img.shields.io/github/release/explosion/spacy-layout.svg?style=flat-square&logo=github&include_prereleases)](https://github.com/explosion/spacy-layout/releases)
[![pypi Version](https://img.shields.io/pypi/v/spacy-layout.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/spacy-layout/)
[![Built with spaCy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg?style=flat-square)](https://spacy.io)

## 📝 Usage

> ⚠️ This package requires **Python 3.10** or above.

```bash
pip install spacy-layout
```

After initializing the `spaCyLayout` preprocessor with an `nlp` object for tokenization, you can call it on a document path to convert it to structured data. The resulting `Doc` object includes layout spans that map into the original raw text and expose various attributes, including the content type and layout features.

```python
import spacy
from spacy_layout import spaCyLayout

nlp = spacy.blank("en")
layout = spaCyLayout(nlp)

# Process a document and create a spaCy Doc object
doc = layout("./starcraft.pdf")

# The text-based contents of the document
print(doc.text)
# Document layout including pages and page sizes
print(doc._.layout)
# Tables in the document and their extracted data
print(doc._.tables)
# Markdown representation of the document
print(doc._.markdown)

# Layout spans for different sections
for span in doc.spans["layout"]:
    # Document section and token and character offsets into the text
    print(span.text, span.start, span.end, span.start_char, span.end_char)
    # Section type, e.g. "text", "title", "section_header" etc.
    print(span.label_)
    # Layout features of the section, including bounding box
    print(span._.layout)
    # Closest heading to the span (accuracy depends on document structure)
    print(span._.heading)
```

If you need to process larger volumes of documents at scale, you can use the `spaCyLayout.pipe` method, which takes an iterable of paths or bytes instead and yields `Doc` objects:

```python
paths = ["one.pdf", "two.pdf", "three.pdf", ...]
for doc in layout.pipe(paths):
    print(doc._.layout)
```

spaCy also allows you to call the `nlp` object on an already created `Doc`, so you can easily apply a pipeline of components for [linguistic analysis](https://spacy.io/usage/linguistic-features) or [named entity recognition](https://spacy.io/usage/linguistic-features#named-entities), use [rule-based matching](https://spacy.io/usage/rule-based-matching) or anything else you can do with spaCy.

```python
# Load the transformer-based English pipeline
# Installation: python -m spacy download en_core_web_trf
nlp = spacy.load("en_core_web_trf")
layout = spaCyLayout(nlp)

doc = layout("./starcraft.pdf")
# Apply the pipeline to access POS tags, dependencies, entities etc.
doc = nlp(doc)
```

### Tables and tabular data

Tables are included in the layout spans with the label `"table"` and under the shortcut `Doc._.tables`. They expose a `layout` extension attribute, as well as an attribute `data`, which includes the tabular data converted to a `pandas.DataFrame`.

```python
for table in doc._.tables:
    # Token position and bounding box
    print(table.start, table.end, table._.layout)
    # pandas.DataFrame of contents
    print(table._.data)
```

By default, the span text is a placeholder `TABLE`, but you can customize how a table is rendered by providing a `display_table` callback to `spaCyLayout`, which receives the `pandas.DataFrame` of the data. This allows you to include the table figures in the document text and use them later on, e.g. during information extraction with a trained named entity recognizer or text classifier.

```python
def display_table(df: pd.DataFrame) -> str:
    return f"Table with columns: {', '.join(df.columns.tolist())}"

layout = spaCyLayout(nlp, display_table=display_table)
```

### Serialization

After you've processed the documents, you can [serialize](https://spacy.io/usage/saving-loading#docs) the structured `Doc` objects in spaCy's efficient binary format, so you don't have to re-run the resource-intensive conversion.

```python
from spacy.tokens import DocBin

docs = layout.pipe(["one.pdf", "two.pdf", "three.pdf"])
doc_bin = DocBin(docs=docs, store_user_data=True)
doc_bin.to_disk("./file.spacy")
```

> ⚠️ **Note on deserializing with extension attributes:** The custom extension attributes like `Doc._.layout` are currently registered when `spaCyLayout` is initialized. So if you're loading back `Doc` objects with layout information from a binary file, you'll need to initialize it so the custom attributes can be repopulated. We're planning on making this more elegant in an upcoming version.
>
> ```diff
> + layout = spacyLayout(nlp)
> doc_bin = DocBin(store_user_data=True).from_disk("./file.spacy")
> docs = list(doc_bin.get_docs(nlp.vocab))
> ```


## 🎛️ API

### Data and extension attributes

```python
layout = spaCyLayout(nlp)
doc = layout("./starcraft.pdf")
print(doc._.layout)
for span in doc.spans["layout"]:
    print(span.label_, span._.layout)
```

| Attribute | Type | Description |
| --- | --- | --- |
| `Doc._.layout` | `DocLayout` | Layout features of the document. |
| `Doc._.pages` | `list[tuple[PageLayout, list[Span]]]` | Pages in the document and the spans they contain. |
| `Doc._.tables` | `list[Span]` | All tables in the document. |
| `Doc._.markdown` | `str` | Markdown representation of the document. |
| `Doc.spans["layout"]` | `spacy.tokens.SpanGroup` | The layout spans in the document. |
| `Span.label_` | `str` | The type of the extracted layout span, e.g. `"text"` or `"section_header"`. [See here](https://github.com/DS4SD/docling-core/blob/14cad33ae7f8dc011a79dd364361d2647c635466/docling_core/types/doc/labels.py) for options. |
| `Span.label` | `int` | The integer ID of the span label. |
| `Span.id` | `int` | Running index of layout span. |
| `Span._.layout` | `SpanLayout \| None` | Layout features of a layout span. |
| `Span._.heading` | `Span \| None` | Closest heading to a span, if available. |
| `Span._.data` | `pandas.DataFrame \| None` | The extracted data for table spans.

### <kbd>dataclass</kbd> PageLayout

| Attribute | Type | Description |
| --- | --- | --- |
| `page_no` | `int` | The page number (1-indexed). |
| `width` | `float` | Page width in pixels. |
| `height` | `float` | Page height in pixels. |

### <kbd>dataclass</kbd> DocLayout

| Attribute | Type | Description |
| --- | --- | --- |
| `pages` | `list[PageLayout]` | The pages in the document. |

### <kbd>dataclass</kbd> SpanLayout

| Attribute | Type | Description |
| --- | --- | --- |
| `x` | `float` | Horizontal offset of the bounding box in pixels. |
| `y` | `float` | Vertical offset of the bounding box in pixels. |
| `width` | `float` | Width of the bounding box in pixels. |
| `height` | `float` | Height of the bounding box in pixels. |
| `page_no` | `int` | Number of page the span is on. |

### <kbd>class</kbd> `spaCyLayout`

#### <kbd>method</kbd> `spaCyLayout.__init__`

Initialize the document processor.

```python
nlp = spacy.blank("en")
layout = spaCyLayout(nlp)
```

| Argument | Type | Description |
| --- | --- | --- |
| `nlp` | `spacy.language.Language` | The initialized `nlp` object to use for tokenization. |
| `separator` | `str` | Token used to separate sections in the created `Doc` object. The separator won't be part of the layout span. If `None`, no separator will be added. Defaults to `"\n\n"`. |
| `attrs` | `dict[str, str]` | Override the custom spaCy attributes. Can include `"doc_layout"`, `"doc_pages"`, `"doc_tables"`, `"doc_markdown"`, `"span_layout"`, `"span_data"`, `"span_heading"` and `"span_group"`. |
| `headings` | `list[str]` | Labels of headings to consider for `Span._.heading` detection. Defaults to `["section_header", "page_header", "title"]`. |
| `display_table` | `Callable[[pandas.DataFrame], str] \| str` | Function to generate the text-based representation of the table in the `Doc.text` or placeholder text. Defaults to `"TABLE"`. |
| `docling_options` | `dict[InputFormat, FormatOption]` | [Format options](https://ds4sd.github.io/docling/usage/#advanced-options) passed to Docling's `DocumentConverter`. |
| **RETURNS** | `spaCyLayout` | The initialized object. |

#### <kbd>method</kbd> `spaCyLayout.__call__`

Process a document and create a spaCy [`Doc`](https://spacy.io/api/doc) object containing the text content and layout spans, available via `Doc.spans["layout"]` by default.

```python
layout = spaCyLayout(nlp)
doc = layout("./starcraft.pdf")
```

| Argument | Type | Description |
| --- | --- | --- |
| `source` | `str \| Path \| bytes \| DoclingDocument` | Path of document to process, bytes or already created `DoclingDocument`. |
| **RETURNS** | `Doc` | The processed spaCy `Doc` object. |

#### <kbd>method</kbd> `spaCyLayout.pipe`

Process multiple documents and create spaCy [`Doc`](https://spacy.io/api/doc) objects. You should use this method if you're processing larger volumes of documents at scale. The behavior of `as_tuples` works like it does in spaCy's [`Language.pipe`](https://spacy.io/api/language#pipe).

```python
layout = spaCyLayout(nlp)
paths = ["one.pdf", "two.pdf", "three.pdf", ...]
docs = layout.pipe(paths)
```

```python
sources = [("one.pdf", {"id": 1}), ("two.pdf", {"id": 2})]
for doc, context in layout.pipe(sources, as_tuples=True):
    ...
```

| Argument | Type | Description |
| --- | --- | --- |
| `sources` | `Iterable[str \| Path \| bytes] \| Iterable[tuple[str \| Path \| bytes, Any]]` | Paths of documents to process or bytes, or `(source, context)` tuples if `as_tuples` is set to `True`. |
| `as_tuples` | `bool` | If set to `True`, inputs should be an iterable of `(source, context)` tuples. Output will then be a sequence of `(doc, context)` tuples. Defaults to `False`. |
| **YIELDS** | `Doc \| tuple[Doc, Any]` | The processed spaCy `Doc` objects or `(doc, context)` tuples if `as_tuples` is set to `True`. |

## 💡 Examples and code snippets

This section includes further examples of what you can do with `spacy-layout`. If you have an example that could be a good fit, feel free to submit a [pull request](https://github.com/explosion/spacy-layout/pulls)!

### Visualize a page and bounding boxes with matplotlib

```python
import pypdfium2 as pdfium
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import spacy
from spacy_layout import spaCyLayout

DOCUMENT_PATH = "./document.pdf"

# Load and convert the PDF page to an image
pdf = pdfium.PdfDocument(DOCUMENT_PATH)
page_image = pdf[2].render(scale=1)  # get page 3 (index 2)
numpy_array = page_image.to_numpy()
# Process document with spaCy
nlp = spacy.blank("en")
layout = spaCyLayout(nlp)
doc = layout(DOCUMENT_PATH)

# Get page 3 layout and sections
page = doc._.pages[2]
page_layout = doc._.layout.pages[2]
# Create figure and axis with page dimensions
fig, ax = plt.subplots(figsize=(12, 16))
# Display the PDF image
ax.imshow(numpy_array)
# Add rectangles for each section's bounding box
for section in page[1]:
    # Create rectangle patch
    rect = Rectangle(
        (section._.layout.x, section._.layout.y),
        section._.layout.width,
        section._.layout.height,
        fill=False,
        color="blue",
        linewidth=1,
        alpha=0.5
    )
    ax.add_patch(rect)
    # Add text label at top of box
    ax.text(
        section._.layout.x,
        section._.layout.y,
        section.label_,
        fontsize=8,
        color="red",
        verticalalignment="bottom"
    )

ax.axis("off")  # hide axes
plt.show()
```
