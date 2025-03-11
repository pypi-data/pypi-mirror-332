import logging
import re

from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File
from typing import MutableMapping, Any

log = logging.getLogger("mkdocs.overview.page.plugin")

class PageWithMetadata:
    meta: MutableMapping[str, Any]
    file: File
    title: str

    def __init__(self, meta: MutableMapping[str, Any], file: File, title: str):
        self.meta = meta
        self.file = file
        self.title = title

class OverviewPagePlugin(BasePlugin):
    
    def __init__(self):
        self.meta = []

    def on_page_markdown(self, markdown, /, *, page, config, files):
        if page.meta:
            title = self.get_title(page, markdown)
            self.meta.append(PageWithMetadata(meta=page.meta, file=page.file, title=title))
            log.info("loaded page with metadata: %s", page.file.src_path)
        return markdown
    
    def get_title(self, page, markdown):
        if page.meta.get('title'):
            return page.meta['title']
        return self.extract_title(markdown)

    def extract_title(self, markdown):
        match = re.search(r'^#\s+(.*)', markdown, re.MULTILINE)
        return match.group(1) if match else "Untitled"

    def on_post_page(self, output_content, page, config):
        placeholder = "{{ overview_table "
        placeholder_end = " }}"
        while placeholder in output_content:
            start, end, keys_str = self.find_placeholder(output_content, placeholder, placeholder_end)
            log.info("Generating overview table for keys: %s", keys_str)
            keys, filters = self.parse_keys_and_filters(keys_str)
            table_html = self.generate_overview_table(keys, filters)
            output_content = output_content.replace(f"{placeholder}{keys_str}{placeholder_end}", table_html)
        return output_content

    def find_placeholder(self, content, placeholder, placeholder_end):
        start = content.find(placeholder) + len(placeholder)
        end = content.find(placeholder_end, start)
        keys_str = content[start:end].strip()
        return start, end, keys_str

    def parse_keys_and_filters(self, keys_str):
        keys_and_filters = keys_str.split(",") if keys_str else []
        filters = {}
        keys = []
        for item in keys_and_filters:
            if "=" in item:
                key, value = item.split("=", 1)
                filters[key.strip()] = value.strip()
            else:
                keys.append(item.strip())
        return keys, filters

    def generate_overview_table(self, keys, filters):
        # Collect all unique meta keys if no specific keys are provided
        if not keys:
            keys = set()
            for meta_file in self.meta:
                keys.update(meta_file.meta.keys())

        # Start the HTML table
        html = self.start_table(keys)

        # Add rows for each file
        for meta_file in self.meta:
            if self.apply_filters(meta_file, filters):
                html += self.generate_table_row(meta_file, keys)

        html += "</tbody></table>"
        return html

    def start_table(self, keys):
        html = "<table><thead><tr><th>Title</th>"
        for key in keys:
            html += f"<th>{key.title()}</th>"
        html += "</tr></thead><tbody>"
        return html

    def apply_filters(self, meta_file, filters):
        return all(meta_file.meta.get(k) == v.replace("-", " ") for k, v in filters.items())

    def generate_table_row(self, meta_file, keys):
        row_url = meta_file.file.url
        html = f"<tr onclick=\"window.location='{row_url}'\" style='cursor:pointer;'>"
        html += f"<td>{meta_file.title}</td>"
        for key in keys:
            html += f"<td>{meta_file.meta.get(key, '').title()}</td>"
        html += "</tr>"
        return html
