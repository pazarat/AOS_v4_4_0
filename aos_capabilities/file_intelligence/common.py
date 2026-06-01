from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List

TEXT_EXTS = {
    '.md','.txt','.yaml','.yml','.json','.jsonl','.toml','.py','.js','.ts','.tsx','.jsx',
    '.cs','.java','.go','.rs','.php','.rb','.kt','.kts','.swift','.c','.cpp','.h','.hpp',
    '.m','.mm','.scala','.dart','.lua','.r','.sh','.bash','.zsh','.ps1','.html','.css',
    '.scss','.sass','.less','.vue','.svelte','.astro','.sql','.xml','.csv','.env',
    '.prisma','.graphql','.gql','.proto','.dockerfile'
}
CODE_EXTS = {
    '.py','.js','.ts','.tsx','.jsx','.cs','.java','.go','.rs','.php','.rb','.kt','.kts',
    '.swift','.c','.cpp','.h','.hpp','.scala','.dart','.lua','.r','.sh','.bash','.zsh','.ps1',
    '.sql','.vue','.svelte','.astro','.prisma','.graphql','.gql','.proto'
}
IGNORE_DIRS = {'.git','__pycache__','.venv','venv','node_modules','.pytest_cache','.mypy_cache','.idea','.vscode','dist','build','.next','coverage','reports','audit'}
# Reserved directories inside workshop/active_project. They are not payload.
AOS_DEFAULT_DIRS = {'runtime_state','.generated','.state'}

LANG_BY_EXT = {
    '.py':'python','.js':'javascript','.jsx':'javascript-react','.ts':'typescript','.tsx':'typescript-react',
    '.cs':'csharp','.java':'java','.go':'go','.rs':'rust','.php':'php','.rb':'ruby','.kt':'kotlin',
    '.swift':'swift','.c':'c','.cpp':'cpp','.h':'c-header','.hpp':'cpp-header','.scala':'scala',
    '.dart':'dart','.lua':'lua','.r':'r','.sh':'shell','.bash':'shell','.zsh':'shell','.ps1':'powershell',
    '.sql':'sql','.prisma':'prisma','.graphql':'graphql','.gql':'graphql','.proto':'protobuf',
    '.html':'html','.css':'css','.vue':'vue','.svelte':'svelte','.astro':'astro',
    '.md':'markdown','.json':'json','.jsonl':'jsonl','.yaml':'yaml','.yml':'yaml','.toml':'toml','.xml':'xml'
}

CONCEPT_GROUPS: Dict[str, List[str]] = {
    'identity_truth': ['entrypoint','contract','truth','source of truth','baseline','identity','mission','مصدر الحقيقة','عقد','هوية'],
    'requirements_prd': ['prd','requirements','specification','acceptance','متطلبات','قبول','مواصفة'],
    'workflow_scenario': ['scenario','workflow','flow','journey','use case','lifecycle','سيناريو','تدفق','رحلة','دورة'],
    'state_event': ['state','status','event','transition','taxonomy','حالة','حدث','انتقال'],
    'permission_security': ['permission','role','audit','security','auth','authorization','access','صلاحية','دور','تدقيق','أمان'],
    'data_contract': ['database','entity','model','api','endpoint','schema','migration','بيانات','كيان','واجهة'],
    'implementation_code': ['class ','def ','function ','interface ','namespace ','import ','using ','export ','async ','await ','كود','تنفيذ'],
    'testing_quality': ['test','testing','quality','coverage','assert','pytest','unit','integration test','اختبار','جودة'],
    'risk_decision': ['risk','decision','adr','tradeoff','constraint','خطر','قرار','قيد'],
    'ux_content': ['ui','ux','screen','component','design','layout','copy','واجهة','تصميم','محتوى'],
}


def rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except Exception:
        return path.as_posix()


def is_binary_sample(data: bytes) -> bool:
    if not data:
        return False
    return b'\0' in data[:4096]


def safe_read_text(path: Path, limit: int = 1_000_000) -> str:
    try:
        data = path.read_bytes()[:limit]
    except Exception:
        return ''
    if is_binary_sample(data):
        return ''
    return data.decode('utf-8', errors='replace')


def tokenize(text: str) -> List[str]:
    return [t.lower() for t in re.findall(r'[A-Za-z_][A-Za-z0-9_]{1,}|[\u0600-\u06FF]{2,}', text)]


def path_role(path: str) -> str:
    low = path.lower()
    name = Path(path).name.lower()
    wrapped = f'/{low}/'
    if '/00_project_local_truth/' in wrapped or name in {'project_contract.json','truth_index.json'}:
        return 'local_project_truth'
    if '/_aos_runtime_project_state/' in wrapped:
        return 'aos_runtime_state'
    if any(x in low for x in ['test','spec']) and Path(low).suffix in CODE_EXTS:
        return 'test_code'
    if any(x in low for x in ['migration','migrations']):
        return 'database_migration'
    if name in {'package.json','pyproject.toml','requirements.txt','csproj','pom.xml','go.mod','cargo.toml'} or low.endswith('.csproj'):
        return 'dependency_manifest'
    if Path(low).suffix in {'.md','.txt'}:
        return 'documentation'
    if Path(low).suffix in {'.json','.yaml','.yml','.toml','.xml'}:
        return 'configuration_or_contract'
    if Path(low).suffix in CODE_EXTS:
        return 'source_code'
    return 'asset_or_other'


def classify_project_condition(records: List[Dict[str, Any]]) -> str:
    payload = [r for r in records if r.get('surface') == 'project_payload']
    if not payload:
        return 'EMPTY_NEW_PROJECT'
    code = [r for r in payload if r.get('is_code')]
    docs = [r for r in payload if r.get('role') == 'documentation' or r.get('language') in {'markdown'}]
    specs = [r for r in payload if any(c in (r.get('concepts') or {}) for c in ['identity_truth','requirements_prd','workflow_scenario'])]
    if specs and not code:
        return 'SPEC_ONLY_PROJECT'
    if code and not docs and not specs:
        return 'EXISTING_UNDOCUMENTED_PROJECT'
    if len(payload) > 250 or len(code) > 100:
        return 'LEGACY_COMPLEX_PROJECT'
    return 'ACTIVE_ENGINEERING_PROJECT'
