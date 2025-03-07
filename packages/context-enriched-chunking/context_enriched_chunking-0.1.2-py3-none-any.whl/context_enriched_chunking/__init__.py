from langchain_text_splitters import RecursiveCharacterTextSplitter

class ContextEnrichedChunking:
    def __init__(self, section_max_words=10, chunk_size=1000, chunk_overlap=100):
        self.section_max_words = section_max_words
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.recursive_text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            is_separator_regex=False,
        )

    def split_text(self, text, title):
        chunks = []
        section = None
        for line in text.strip().splitlines():
            if len(line.split()) <= self.section_max_words:
                section = line
                chunk = f"Content: {section}"
                if title:
                    chunk = f"Title: {title}\n" + chunk
                chunks.append(chunk)
            else:
                contents = self.recursive_text_splitter.split_text(line)
                n_contents = len(contents)
                for i, content in enumerate(contents):
                    part = f"(Part {i+1}/{n_contents}) " if n_contents > 1 else ""
                    chunk = f"Content: {part}{content}"
                    if section:
                        chunk = f"Section: {section}\n" + chunk
                    if title:
                        chunk = f"Title: {title}\n" + chunk
                    chunks.append(chunk)
        return chunks