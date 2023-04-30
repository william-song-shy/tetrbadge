# Tetr Badge

本项目为 [Zhengfourth/TetrioRatingColor](https://github.com/Zhengfourth/TetrioRatingColor) 的 Python 改版，得到了原作者的许可。

## 部署地址

<https://tetr.rotriw.com/>

## 用法

API 格式保留了原项目的格式。

| 参数    | 可选值                          | 含义                         |
|-------|------------------------------|----------------------------|
| user  | 必选，小写字母                      | 用户名                        |
| style | 可选，默认为 for-the-badge         | shields.io 的样式             |
| st    | 可选，style 的缩写 ~~（所以这个是什么目的）~~ | f1 : flat；f2 : flat-square |

## 示例

<https://tetr.rotriw.com/?user=xcyle>：![https://tetr.rotriw.com/?user=xcyle](https://tetr.rotriw.com/?user=xcyle)

<https://tetr.rotriw.com/?user=xcyle&st=f2>：![https://tetr.rotriw.com/?user=xcyle&st=f2](https://tetr.rotriw.com/?user=xcyle&st=f2)

<https://tetr.rotriw.com/?user=xcyle&style=plastic>：![https://tetr.rotriw.com/?user=xcyle&style=plastic](https://tetr.rotriw.com/?user=xcyle&style=plastic)

## Todo

- [x] 复刻原项目内容
- [ ] 增加查询缓存
- [ ] 增加 40L，Blitz 的 PB 徽章

## 杂谈

tetr.io API 的缓存只有 300 s。666。