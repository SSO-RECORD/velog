import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@ssossosso'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 피드 항목 개수 출력
print(f"Number of entries in feed: {len(feed.entries)}")
for entry in feed.entries:
    print(f"Entry title: {entry.title}")
    
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-') #슬래시를 대시로 대체
    file_name = file_name.replace('\\', '-') #백슬래시를 대시로 대체
    #필요에 따라 추가 문자 대체
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)

    # 새 글이거나, 기존 글과 내용이 달라진 경우 업데이트
    needs_update = False
    content = entry.description.strip()

    # 파일이 이미 존재하지 않으면 생성
    if not os.path.exists(file_path):
        needs_update = True
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            old_content = file.read().strip()
            if old_content != content:
                needs_update = True
                
    if needs_update:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)  # 글 내용을 파일에 작성
        # 깃허브에 파일 추가
        repo.git.add(file_path)
        repo.git.commit('-m', f'Update post: {entry.title}')
        print(f"Updated file: {file_path}")
    else:
        print(f"No changes for: {file_path}")
