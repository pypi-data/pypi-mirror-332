__version__ = "2.6.6"


def string_to_binary(s):
    # 将字符串转换为二进制表示，使用 UTF-8 编码
    return ''.join(format(ord(char), '016b') for char in s)


def binary_to_string(b):
    # 将二进制表示转换回字符串
    chars = [chr(int(b[i:i + 16], 2)) for i in range(0, len(b), 16)]
    return ''.join(chars)


def segment_binary(binary_str):
    original_str = binary_to_string(binary_str)

    # 计算每个字符的平均二进制长度
    segment_length = len(binary_str) // len(original_str)

    # 分段
    segments = [binary_str[i:i + segment_length] for i in range(0, len(binary_str), segment_length)]
    return segments


if __name__ == "__main__":
    original_string = "Hello EasyCryptographer"

    binary_representation = string_to_binary(original_string)
    print(f"Binary representation: {binary_representation}")

    segments = segment_binary(binary_representation)
    print(f"Segments: {segments}")

    combined_binary_str = ''.join(segments)
    print(f"Combined binary string: {combined_binary_str}")

    reconstructed_string = binary_to_string(combined_binary_str)
    print(f"Reconstructed string: {reconstructed_string}")
