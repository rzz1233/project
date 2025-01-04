import pytest

# test_example.py
def test_addition():
    assert 1 + 1 == 2


# 你可以使用 @pytest.mark 为测试添加标记，便于分类和选择运行

# 运行命令 pytest -m smoke

@pytest.mark.smoke
def test_addition():
    assert 1 + 1 == 2
