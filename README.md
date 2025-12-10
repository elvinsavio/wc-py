# wc — Word and Line Counter

A command-line utility for counting words and/or lines in one or more files, or across all files in a directory.

---

## Usage

```bash
wc [OPTIONS] FILENAMES...
````

* `FILENAMES` may be:

  * One file
  * Multiple files
  * One directory (directories cannot be combined with other paths)

---

## Description

`wc` counts words and/or lines in files.

* When multiple files are provided, counts are shown per file unless `--collection` is used.
* When a directory is provided, all files inside the directory are scanned.

---

## Options

| Option | Long Option    | Description                                         |
| ------ | -------------- | --------------------------------------------------- |
| `-c`   | `--collection` | Show a collective (combined) count across all files |
| `-w`   | `--word`       | Show word count only                                |
| `-l`   | `--line`       | Show line count only                                |

### Option Notes

* If **neither `-w` nor `-l`** is specified, both word and line counts are shown.
* `--collection` **cannot be combined** with `-w` or `-l`. If used together, a warning is issued and `-w` / `-l` are ignored.

---

## Behavior Summary

### Single File

```bash
wc file.txt
```

Shows word and line counts for `file.txt`.

---

### Multiple Files

```bash
wc a.txt b.txt c.txt
```

Shows counts for each file individually.

---

### Multiple Files (Collected)

```bash
wc -c a.txt b.txt c.txt
```

Shows a single combined count for all files.

---

### Directory

```bash
wc my_folder/
```

Counts words and lines across all files in `my_folder`.

---

### Directory (Collected)

```bash
wc -c my_folder/
```

Shows a collective total for all files in the directory.

---

## Invalid Usage

| Case                                             | Result                       |
| ------------------------------------------------ | ---------------------------- |
| No filenames provided                            | Error                        |
| Multiple paths including more than one directory | Error                        |
| Multiple directories at once                     | Error                        |
| `-c` used with `-w` or `-l`                      | Warning; `-w` / `-l` ignored |

---

## Examples

Show words and lines:

```bash
wc file.txt
```

Words only:

```bash
wc -w file.txt
```

Lines only:

```bash
wc -l file.txt
```

Multiple files, combined:

```bash
wc -c file1.txt file2.txt
```

Directory scan:

```bash
wc src/
```

---

## Exit Conditions

* Raises an error if:

  * No files are provided
  * More than one directory is supplied
* Prints warnings for incompatible options

```
```
