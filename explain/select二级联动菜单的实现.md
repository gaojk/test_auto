# Select2样式库
引用 select2 样式库 [官方地址](https://select2.org/)

导入css和js
```html
<link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.7/css/select2.min.css" rel="stylesheet"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.7/js/select2.min.js"></script>
```

添加select2的样式--select2-single
```html
<div style="margin-top: 20px;">
    <label style="float: left">项目：</label>
    <select class="form-control select2-single" id="selectProject" style="width: 180px">
    </select>
    <br>
    <label style="float: left">模块：</label>
    <select class="form-control select2-single" id="selectModule" style="width: 180px">
    </select>
</div>
```

一个接口同时取到项目和模块, 后端的调用接口--views.py
```python

```
