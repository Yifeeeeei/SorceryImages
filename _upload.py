import os
import shutil


def copy_and_overwrite_file(source, destination):
    try:
        # Copy the file, using `shutil.copyfile` which will overwrite by default

        shutil.copyfile(source, destination)
        # print(
        #     f"The file has been copied and overwritten from {source} to {destination}."
        # )
    except Exception as e:
        print(f"An error occurred: {e}")


def add_commit_and_push():
    # return
    os.system("git add .")
    os.system("git commit -m 'update'")
    os.system("git push")


target_dir = "images"
source_dir = "output"
cnt = 0
max_cnt = 50

for type_dir in os.listdir(source_dir):
    if not os.path.isdir(os.path.join(source_dir, type_dir)):
        continue
    for ele_dir in os.listdir(os.path.join(source_dir, type_dir)):
        if not os.path.isdir(os.path.join(source_dir, type_dir, ele_dir)):
            continue
        for img in os.listdir(os.path.join(source_dir, type_dir, ele_dir)):
            if not img.endswith(".jpg"):
                continue

            source = os.path.join(source_dir, type_dir, ele_dir, img)
            destination = os.path.join(target_dir, type_dir, ele_dir, img)
            if not os.path.exists(os.path.join(target_dir, type_dir, ele_dir)):
                os.makedirs(os.path.join(target_dir, type_dir, ele_dir))
            cnt += 1
            copy_and_overwrite_file(source, destination)
            if cnt >= max_cnt:
                add_commit_and_push()
                cnt = 0
print("Done!")
