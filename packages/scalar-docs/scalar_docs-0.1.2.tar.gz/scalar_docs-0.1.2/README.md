# scalar_py

`scalar_py` is a Python wrapper for the [Scalar API](https://scalar.com/), a powerful tool for generating and managing API documentation. This library allows you to interact with the Scalar API to fetch, customize, and render API documentation in your Python applications.

## Installation

To install `scalar-docs`, you can use `pip`:

```bash
pip install scalar-docs
```

If you'd like to install the example dependencies for specific use cases, you can do so by running:

```bash
pip install scalar_py[django_example]
pip install scalar_py[fastapi_example]
pip install scalar_py[flask_example]
```

These optional dependencies are provided for working with examples built with Django, FastAPI, and Flask.

## Usage

The `scalar_py` library provides a set of data models, helper functions, and utilities to interact with Scalar's API documentation services. It allows you to configure and customize your API reference UI, handle API key authentication, and fetch content from Scalar's CDN or your own URLs.

### Basic Example

```python
from scalar import Options, Spec, ApiKeyAuth, api_reference_html

# Configure your options
options = Options(
    spec=Spec(url="https://example.com/openapi-spec.json"),
    authentication=ApiKeyAuth(token="your-api-key")
)

# Generate HTML for the API Reference
html_content = api_reference_html(options)

# Now you can save or render the HTML content as needed
print(html_content)
```

### Customizing the API Reference

You can customize the API reference with several options, such as:

- **CDN URL**: You can change the Scalar CDN URL to a custom one using the `cdn` option.
- **Theme**: Customize the theme of the documentation (e.g., `light` or `dark` modes) using the `theme` option.
- **Authentication**: You can set up API key or OAuth2 authentication using the `authentication` option.

### Example: Customize Your Documentation's Theme

```python
from scalar import Options, CustomOptions, api_reference_html

options = Options(
    custom_options=CustomOptions(page_title="Custom API Reference"),
    darkMode=True
)

html_content = api_reference_html(options)
print(html_content)
```

## Available Data Models

### `Options`

The `Options` dataclass holds the main configuration for your API reference page. Here's a breakdown of its key attributes:

- **`cdn`**: The URL for the CDN that hosts Scalar's resources (default: `"https://cdn.jsdelivr.net/npm/@scalar/api-reference"`).
- **`layout`**: The layout style for the documentation (e.g., `"modern"`, `"classic"`).
- **`spec`**: The OpenAPI specification, which can be provided as a URL or raw content (JSON string).
- **`specContent`**: The OpenAPI spec content (can be a callable, dict, or string).
- **`proxyUrl`**: Proxy URL for making requests through a proxy server (default: `"https://proxy.scalar.com"`).
- **`isEditable`**: Whether the documentation is editable (default: `False`).
- **`showSidebar`**: Whether to show the sidebar (default: `True`).
- **`hideModels`**: Whether to hide models in the documentation (default: `False`).
- **`hideDownloadButton`**: Whether to hide the download button (default: `False`).
- **`hideSearch`**: Whether to hide the search feature (default: `False`).
- **`darkMode`**: Whether to use dark mode for the documentation (default: `False`).
- **`hideDarkModeToggle`**: Whether to hide the toggle for dark mode (default: `False`).
- **`customCss`**: A string containing custom CSS to inject into the documentation.
- **`searchHotKey`**: The hotkey for searching (default: `"k"`).
- **`baseServerURL`**: The base server URL for the API.
- **`servers`**: A list of `ServerOptions` objects that represent the available servers.
- **`favicon`**: The URL or file path to the favicon.
- **`hiddenClients`**: A list or boolean value specifying which clients should be hidden (e.g., `["http", "curl"]` or `True` to hide all).
- **`authentication`**: Authentication options (can include `ApiKeyAuth` or `OAuth2Auth`).
- **`withDefaultFonts`**: Whether to include default fonts (default: `True`).
- **`defaultOpenAllTags`**: Whether to open all tags by default in the documentation (default: `False`).
- **`theme`**: The theme for the documentation (e.g., `"default"`, `"custom"`).
- **`metaData`**: Metadata options for the documentation (e.g., OpenGraph tags, Twitter card data).
- **`hideTestRequestButton`**: Whether to hide the "Test Request" button in the API documentation (default: `False`).
- **`pathRouting`**: Custom routing for paths (if needed).
- **`hideClientButton`**: Whether to hide the client button (default: `False`).
- **`custom_options`**: Custom options like the page title (default: `"API Reference"`).

### `Spec`

- **`content`**: Optional; the content of the OpenAPI spec in JSON format.
- **`url`**: Optional; the URL to fetch the OpenAPI spec from.

### `MetaDataOptions`

- **`title`**: The title of the page.
- **`description`**: The description of the API reference page.
- **`ogTitle`**, **`ogDescription`**, **`ogImage`**: OpenGraph metadata for social sharing.
- **`twitterCard`**: Twitter card metadata.

### `ServerOptions`

- **`url`**: The URL of the server.
- **`description`**: A description of the server.

### `Authentication`

- **`preferredSecurityScheme`**: The preferred security scheme for the API (e.g., `"apiKey"`, `"OAuth2"`).
- **`apiKey`**: An instance of `ApiKeyAuth` for API key authentication.
- **`oAuth2`**: An instance of `OAuth2Auth` for OAuth2 authentication.

### `ApiKeyAuth` & `OAuth2Auth`

- **`ApiKeyAuth`**: Requires a `token` attribute to authenticate API requests.
- **`OAuth2Auth`**: Requires a `clientId` and optionally a list of `scopes` for OAuth2 authentication.

## Helper Functions

- **`safe_json_configuration(options)`**: Serializes your options to JSON and escapes double quotes for safe HTML embedding.
- **`specContent_handler(specContent)`**: Handles different types of `specContent`, whether it's a string, dictionary, or callable.
- **`ensure_file_url(file_path)`**: Converts a file path into a valid `file://` URL if necessary.
- **`fetch_content_from_url(url)`**: Fetches content from a URL.
- **`read_file_from_url(file_url)`**: Reads content from a local file (via `file://` URL).
- **`api_reference_html(options)`**: Generates the full HTML content for the API reference page.

## Customizing the UI

You can also inject custom CSS into the generated documentation using the `customCss` field in the `Options` object. For example:

```python
options = Options(customCss="body { font-family: Arial, sans-serif; }")
html_content = api_reference_html(options)
```

## License

This library is released under the MIT License. See the [LICENSE](LICENSE) file for more information.
