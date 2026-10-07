#!/usr/bin/env python3
"""Verify a pinned identity-release bundle offline; never compare with latest."""
import argparse
import hashlib
import json
import re
from pathlib import Path


def verify(directory, tag=None):
    directory = Path(directory)
    manifest = json.loads((directory / 'release-manifest.json').read_text())
    version = manifest['version']
    if not re.fullmatch(r'\d+(?:\.\d+)+', version):
        raise ValueError('Invalid identity specification version')
    if tag and tag != f'id-v{version}':
        raise ValueError('Tag does not match manifest version')
    if not re.fullmatch(r'[0-9a-f]{40}', manifest['source_revision']):
        raise ValueError('Source revision must be a full platform commit SHA')
    if manifest['source_repository'] != 'no-fait/platform':
        raise ValueError('Unexpected source repository')
    expected = {
        'SPECIFICATION.md', f'resolution_input_contract_v{version}.json',
        f'resolution_match_taxonomy_v{version}.json',
        f'releases/id-v{version}.md', 'verify-identity-release.py',
    }
    if set(manifest['files']) != expected:
        raise ValueError('Manifest must contain exactly the expected release files')
    for name, digest in manifest['files'].items():
        data = (directory / name).read_bytes()
        if not data or hashlib.sha256(data).hexdigest() != digest:
            raise ValueError(f'Missing, empty or modified release asset: {name}')
    for name in expected:
        if name.endswith('.json'):
            if json.loads((directory / name).read_text()).get('version') != version:
                raise ValueError(f'Asset version disagrees with manifest: {name}')
    expected_tag = f'**Release Tag:** `id-v{version}`'
    for name in ('SPECIFICATION.md', f'releases/id-v{version}.md'):
        if expected_tag not in (directory / name).read_text():
            raise ValueError(f'Release label disagrees with manifest: {name}')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory')
    parser.add_argument('--tag')
    args = parser.parse_args()
    try:
        result = verify(args.directory, args.tag)
        print(f"Verified id-v{result['version']} from platform@{result['source_revision']}")
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f'Identity release verification failed: {error}\n')
