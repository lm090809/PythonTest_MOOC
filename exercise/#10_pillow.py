import os
from PIL import Image


def analyze_image(file_path):
    """
    分析图片内容并识别异常特征。

    :param img: 图像对象
    :return: 异常特征的描述字符串或None（如果图片正常）
    """
    img = Image.open(file_path)
    # 检查分辨率
    width, height = img.size
    print(f"图片分辨率：{width}x{height}")
    if width < 100 or height < 100:  # 假设分辨率小于100x100是异常的
        return "分辨率异常（太小）"

    # 检查颜色
    try:
        img = img.convert("RGB")  # 转换为RGB模式
        r, g, b = img.getpixel((0, 0))  # 获取左上角像素的颜色
        print(r,g,b)
        if r == g == b == 0:  # 检查是否为全黑图片
            return "颜色异常（全黑）"
        if r == g == b == 255:  # 检查是否为全白图片
            return "颜色异常（全白）"
    except Exception as e:
        print(f"无法分析图片颜色：{e}")
        return None


def process_images_in_folder(folder_path):
    """
    处理指定文件夹中的所有图片文件。

    :param folder_path: 文件夹的路径
    """
    all_pic_count = 0
    ano_pic_count = 0
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            all_pic_count +=1
            print("图片",all_pic_count,file_name)
            file_path = os.path.join(folder_path, file_name)
            # img = read_image(file_path)
            anomaly_description = analyze_image(file_path)
            if anomaly_description:
                ano_pic_count += 1
                print(f"异常图片：{file_path} - {anomaly_description}")
            print("\n")
                # 这里可以添加处理异常图片的代码，例如移动文件或记录日志
    print("all Pic:", all_pic_count)
    print("anomally Pic:", ano_pic_count)

# 主函数
if __name__ == "__main__":
    # 指定要处理的图片文件夹路径
    folder_path = r"C:\02 Software\exercise\picture"
    process_images_in_folder(folder_path)