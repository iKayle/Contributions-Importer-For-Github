import git
from git_contributions_importer import *
# Your private repo or Bitbucket repo
repo = git.Repo("/Work/eunerd/guio-front")
# Your mock repo
mock_repo = git.Repo("/Work/importer-for-git/mock_repo")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['kayle.barrt@gmail.com', 'kayle.barreto@eunerd.com.br'])
importer.import_repository()