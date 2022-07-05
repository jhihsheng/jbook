---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---
# Add flow charts in JB
First, install the Sphinx extensions
```
pip install sphinxcontrib-mermaid
pip install sphinxcontrib-wavedrom
```
Then, in the `_config.yml` file, add 
```
sphinx:
  extra_extensions:
    - sphinxcontrib.mermaid
    - sphinxcontrib.wavedrom
    
```

## Mermaid flow chart

You can start to use the `mermaid` systax to make your own flow chart :)
### Top down flow chart
````
```{mermaid}

flowchart TD
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```
````
The result is 
```{mermaid}

flowchart TD
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```

````
```{mermaid}
flowchart TD
    
    A:::someclass --> B:::someclass
    classDef someclass fill:#f96,stroke:#333;

```
````
```{mermaid}
flowchart TD
    
    A:::someclass --> B:::someclass
    classDef someclass fill:#f96,stroke:#333;

```
### Left-Right flow chart
````
```{mermaid}
flowchart LR
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```
````
The result is 
```{mermaid}

flowchart LR
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```
## Dropdown
````
```{dropdown} Here's my dropdown
And here's my dropdown content
```
````

```{dropdown} Here's my dropdown
And here's my dropdown content
```
