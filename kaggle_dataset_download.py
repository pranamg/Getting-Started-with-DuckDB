# pip install --upgrade --user kaggle
import sys, subprocess, os
try:
    from kaggle.api.kaggle_api_extended import KaggleApi
except Exception as e:
    print('kaggle package not available, installing...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', 'kaggle'])
    # try import again
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except Exception as e2:
        print('Failed to import kaggle after install:', e2)
        sys.exit(1)

api = KaggleApi()
api.authenticate()

out_dir = '/workspaces/Getting-Started-with-DuckDB/chapter_04'
os.makedirs(out_dir, exist_ok=True)

files_to_try = ['Books_rating.zip','books_data.zip','Books_rating.csv','books_data.csv']
for fname in files_to_try:
    try:
        print('\nDownloading:', fname)
        api.dataset_download_file('mohamedbakhet/amazon-books-reviews', fname, path=out_dir, force=True, quiet=False)
    except Exception as exc:
        print('  -> error for', fname, ':', exc)

print('\n--- contents of', out_dir, '---')
for entry in sorted(os.listdir(out_dir)):
    print(entry)