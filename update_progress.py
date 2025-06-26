import os

ROOT_DIRS = ['Microsoft','Google','Leetcode']
PROGRESS_FILE = 'progress.md'

def extract_problems():
  sections = {}
  for root  in ROOT_DIRS:
    if not os.path.exists(root):
      continue
    files = [f for f in os.listdir(root) if f.endswith('.py')]
    sections[root.capitalize()] = []
    for file in sorted(files):
      file_path = os.path.join(root,file)
      with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        done = '# ✅ Completed' in content
        status = '[√]' if done else '[ ]'
        sections[root.capitalize()].append(f"- {status} {file}")

  return sections


def write_progress(sections):
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
      f.write('# 📈 Algorithm Practice Progress\n\n')
      f.write('> This list is automatically generated from your code files.  \n')
      f.write('> Completed problems are checked ✅\n\n')
      for section, items in sections.items():
          f.write(f'## {section}\n\n')
          for item in items:
              f.write(item + '\n')
          f.write('\n')


if __name__ == '__main__':
    write_progress(extract_problems())
    print("✅ progress.md updated.")