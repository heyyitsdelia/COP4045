import unittest


class Entry:
	def __init__(self, name: str, parent: "Folder | None" = None) -> None:
		if not isinstance(name, str):
			raise TypeError("name must be a string")

		self.name = name
		self._parent: Folder | None = None
		if parent is not None:
			parent.add(self)

	def parent(self) -> "Folder | None":
		return self._parent

	def size(self) -> int:
		raise NotImplementedError("Entry subclasses must implement size()")

	def absolute_path(self) -> list["Entry"]:
		if self._parent is None:
			return [self]
		return [self] + self._parent.absolute_path()


class File(Entry):
	def __init__(
		self, name: str, bytes_used: int, parent: "Folder | None" = None
	) -> None:
		if not isinstance(bytes_used, int):
			raise TypeError("bytes_used must be an integer")
		if bytes_used < 0:
			raise ValueError("bytes_used cannot be negative")

		super().__init__(name, parent)
		self.bytes_used = bytes_used

	def size(self) -> int:
		return self.bytes_used


class Folder(Entry):
	def __init__(self, name: str, parent: "Folder | None" = None) -> None:
		super().__init__(name, parent)
		self._children: list[Entry] = []

	def add(self, entry: Entry) -> None:
		if not isinstance(entry, Entry):
			raise TypeError("Folder children must be Entry objects")
		if entry is self:
			raise ValueError("A folder cannot contain itself")

		ancestor: Folder | None = self
		while ancestor is not None:
			if ancestor is entry:
				raise ValueError("Adding this entry would create a cycle")
			ancestor = ancestor.parent()

		previous_parent = entry.parent()
		if previous_parent is self:
			return
		if previous_parent is not None:
			previous_parent._children.remove(entry)

		entry._parent = self
		self._children.append(entry)

	def size(self) -> int:
		return sum(child.size() for child in self._children)

	def children(self) -> tuple[Entry, ...]:
		return tuple(self._children)


def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
	"""Return files at least minimum_size bytes, searching folders recursively."""
	if isinstance(entry, File):
		return [entry] if entry.size() >= minimum_size else []
	if isinstance(entry, Folder):
		return [
			file
			for child in entry.children()
			for file in find_large_files(child, minimum_size)
		]
	raise TypeError("entry must be a File or Folder")


def build_sample_hierarchy() -> tuple[Folder, File]:
	root = Folder("root")
	root.add(File("readme.txt", 50))
	documents = Folder("documents", root)
	projects = Folder("projects", documents)
	projects.add(File("notes.txt", 500))
	assets = Folder("assets", projects)
	large_file = File("archive.zip", 1200, assets)
	return root, large_file


class EntryHierarchyTests(unittest.TestCase):
	def setUp(self) -> None:
		self.root, self.large_file = build_sample_hierarchy()

	def test_file_size_and_nonnegative_validation(self) -> None:
		self.assertEqual(self.large_file.size(), 1200)
		with self.assertRaises(ValueError):
			File("invalid.bin", -1)

	def test_folder_size_includes_nested_entries(self) -> None:
		self.assertEqual(self.root.size(), 1750)

	def test_children_returns_tuple(self) -> None:
		self.assertIsInstance(self.root.children(), tuple)
		self.assertEqual([entry.name for entry in self.root.children()], ["readme.txt", "documents"])

	def test_find_large_files_on_file(self) -> None:
		self.assertEqual(find_large_files(self.large_file, 1200), [self.large_file])
		self.assertEqual(find_large_files(self.large_file, 1201), [])

	def test_find_large_files_at_two_thresholds(self) -> None:
		self.assertEqual(
			find_large_files(self.root, 1000),
			[self.large_file],
		)
		self.assertEqual(
			[file.name for file in find_large_files(self.root, 400)],
			["notes.txt", "archive.zip"],
		)

	def test_absolute_path_runs_from_entry_to_root(self) -> None:
		self.assertEqual(
			[entry.name for entry in self.large_file.absolute_path()],
			["archive.zip", "assets", "projects", "documents", "root"],
		)


def show_hierarchy_demo() -> None:
	root, large_file = build_sample_hierarchy()
	print(f"Total size of {root.name}: {root.size()} bytes")
	for threshold in (1000, 400):
		names = [file.name for file in find_large_files(root, threshold)]
		print(f"Files at least {threshold} bytes: {names}")
	print("Absolute path:", [entry.name for entry in large_file.absolute_path()])


if __name__ == "__main__":
	show_hierarchy_demo()
	unittest.main()
