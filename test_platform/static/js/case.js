//初始化 “项目>模块” 二级联动菜单
var SelectInit = function (defaultProjectId, defaultModuleId) {
    var cmbProject = document.getElementById("selectProject");
    var cmbModule = document.getElementById("selectModule");

    var dataList = [];

    //设置默认选项
    function setDefaultOption(obj, id) {
        for (var i = 0; i < obj.options.length; i++) {
            if (obj.options[i].value == id) {
                obj.selectedIndex = i;
                return;
            }
        }
    }

    //创建下拉选项
    function addOption(cmb, obj) {
        console.log("输出选项", obj)
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = obj.name;
        option.value = obj.id;
    }

    //改变项目
    function changeProject() {
        cmbModule.options.length = 0;
        console.log("项目默认选项的索引", cmbProject.selectedIndex);
        var pid = cmbProject.options[cmbProject.selectedIndex].value;
        console.log("这个才是真的项目id", pid);

        for (let i = 0; i < dataList.length; i++) {
            if(dataList[i].id == pid) {
                let modules = dataList[i].moduleList;
                console.log("对应的模块列表", modules);
                for(let j=0; j< modules.length; j++){
                    addOption(cmbModule, modules[j]);
                }
            }

        }

        setDefaultOption(cmbModule, defaultModuleId);
    }

    function getSelectData() {
        // 调用获取select数据列表
        $.get("/project/get_project_list/", {}, function (resp) {
            if (resp.status === 10200) {
                dataList = resp.data;
                console.log("想要的数据格式-->", dataList);
                //遍历项目
                for (var i = 0; i < dataList.length; i++) {
                    console.log("每一个项目的数据", dataList[i]);
                    addOption(cmbProject, dataList[i]);
                }

                setDefaultOption(cmbProject, defaultProjectId);
                changeProject();
                cmbProject.onchange = changeProject;
            }

            setDefaultOption(cmbProject, defaultProjectId);

        });
    }

    // 调用getSelectData函数
    getSelectData();

};