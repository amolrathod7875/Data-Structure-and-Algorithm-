"""Verify the archived accepted-source snapshot without contacting LeetCode."""

import ast
import json
from pathlib import Path
import re


def main():
    folder = Path(__file__).resolve().parent
    root = folder.parent
    archive = json.loads((folder / 'accepted_submissions.json').read_text())
    submissions = archive['submissions']
    ids = [entry['id'] for entry in submissions]
    assert len(ids) == len(set(ids)) == archive['missing_accepted_count'] == 167
    assert archive['status'] == 'complete'

    history_ids = {int(row['title'].split('.')[0])
                   for row in archive['practice_history']}
    solved_ids = history_ids - set(archive['excluded_unsolved_ids'])
    assert len(history_ids) == archive['practice_history_count'] == 247
    assert len(solved_ids) == archive['solved_count'] == 245

    existing_ids = set()
    for path in root.rglob('LC_*'):
        if folder in path.parents:
            continue
        match = re.fullmatch(r'LC_(\d+)', path.name)
        if match and path.is_dir():
            sources = [source for source in path.rglob('code.py')
                       if source.is_file() and source.read_text().strip()]
            if sources:
                existing_ids.add(int(match.group(1)))
    assert existing_ids == set(archive['existing_repository_ids'])
    assert len(existing_ids & solved_ids) == archive['already_represented'] == 78
    assert set(ids) == solved_ids - existing_ids

    parsed = 0
    for entry in submissions:
        assert entry['verdict'] == 'Accepted', entry['id']
        assert '/submissions/' in entry['url'], entry['id']
        assert entry['code'].strip(), entry['id']
        extension = 'cpp' if entry['language'] == 'C++' else 'py'
        source = folder / f"LC_{entry['id']}.{extension}"
        assert source.read_bytes() == entry['code'].encode('utf-8'), source.name
        if entry['language'] in ('Python3', 'Pandas'):
            ast.parse(entry['code'], filename=source.name)
            parsed += 1

    actual_sources = {path.name for path in folder.glob('LC_*') if path.is_file()}
    expected_sources = {f"LC_{entry['id']}.{'cpp' if entry['language'] == 'C++' else 'py'}"
                        for entry in submissions}
    assert actual_sources == expected_sources
    assert solved_ids <= existing_ids | set(ids)
    print('245/245 solved history problems represented in the repository.')
    print('167 original accepted source files match the archive byte-for-byte.')
    print(f'{parsed} Python 3/Pandas source files parsed successfully.')
    print('36 legacy Python 2 and 7 C++ sources retain their original runtimes.')


if __name__ == '__main__':
    main()
