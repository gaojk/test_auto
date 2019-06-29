//创建下拉选项
function cmbAddOption(cmb, obj){
    let option = document.createElement("option");
    cmb.options.add(option);
    option.innerHTML = obj.name;
    option.value = obj.id;
}

// 清除下拉选项
function clearOption(cmb){
    for(let i=0;i<=cmb.length+1;i++){
        cmb.options.remove(cmb[i]);
    }
}

// 获取项目列表
var ProjectInit = function(_cmbProject){
    var cmbProject = document.getElementById(_cmbProject);

    function getProjectListInfo(){
        // 获取某个用例信息
        $.get("/project/get_project_list/", {}, function(resp){
            if(resp.status == 10200){
                console.log(resp.data);
                let dataList = resp.data;
                for(let i=0; i<dataList.length;i++){
                    cmbAddOption(cmbProject, dataList[i]);
                }
            }else{
                window.alert(resp.message)
            }
        });
    }

    getProjectListInfo();
};

// 获取某一个项目的模块列表
var ModuleInit = function(_cmbModule, pid){
    var cmbModule = document.getElementById(_cmbModule);

    function getModuleListInfo(){
        // 获取某个用例信息
        $.post("/module/get_module_list/", {"pid": pid}, function(resp){
            if(resp.status == 10200){
                console.log(resp.data);
                let dataList = resp.data;
                clearOption(cmbModule);
                for(let i=0; i<dataList.length;i++){
                    cmbAddOption(cmbModule, dataList[i]);
                }
                $("#selectModule").selectpicker("refresh");
            }else{
                window.alert(resp.message)
            }
        });
    }

    getModuleListInfo();
};