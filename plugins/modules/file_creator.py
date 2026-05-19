from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: file_creator
short_description: Creates a file with specified content on the remote host.
version_added: "1.0.0"
description: This module ensures that a file exists at a specific path with specific content.
options:
    path:
        description: The absolute path to the file to create.
        required: true
        type: path
    content:
        description: The content to write into the file.
        required: true
        type: str
    force_change:
        description: If set to true, ensures the file is always reported as changed.
        required: false
        type: bool
        default: false
author:
    - Your Name (@yourGitHubHandle)
'''
EXAMPLES = r'''
- name: Create test file
  my_own_namespace.yandex_cloud_elk.file_creator:
    path: /tmp/my_test_file.txt
    content: "Hello from my custom module!"
'''
RETURN = r'''
path_written:
    description: The path of the file that was processed.
    type: str
    returned: always
content_written:
    description: The content that was written to the file.
    type: str
    returned: always
'''
from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=True),
        force_change=dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        path_written='',
        content_written=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    path = module.params['path']
    content = module.params['content']
    force_change = module.params['force_change']

    result['path_written'] = path
    result['content_written'] = content

    current_content = ""
    file_exists = os.path.exists(path)

    if file_exists:
        with open(path, 'r') as f:
            current_content = f.read()

    if current_content != content or not file_exists or force_change:
        try:
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
        except Exception as e:
            module.fail_json(msg=f"Failed to write file {path}: {e}", **result)
    else:
        result['changed'] = False

    module.exit_json(**result)

if __name__ == '__main__':
    run_module()
