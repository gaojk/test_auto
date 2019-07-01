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

//获取用例信息
var TestCaseInit = function () {

    var url = document.location; //获取当前的url
    console.log("url:", url);
    // 打印url方法
    // var url = window.location.href;
    // var url = self.location.href;
    // var url = document.location;
    var cid =  url.pathname.split("/")[3];

    $.post("/testcase/get_case_info/",
    {
        cid: cid,
    },
    function (resp, status) {
        console.log("返回的结果", resp.data);
        var result = resp.data;

        //请求URL
        document.querySelector("#req_url").value = resp.data.url;

        //请求方法
        if (result.method == 1){
            document.querySelector("#get").setAttribute("checked", "");
        }else if (result.method == 2) {
            document.querySelector("#post").setAttribute("checked", "");
        }else if (result.method == 3){
            document.querySelector("#put").setAttribute("checked", "");
        } else if (result.method == 4){
            document.querySelector("#delete").setAttribute("checked", "");
        }

        //请求头
        document.querySelector("#header").value = result.header;

        //请求参数类型
        if (result.parameter_type == 1) {
            document.querySelector("#form").setAttribute("checked", "");
        }
        else if (result.parameter_type == 2) {
            document.querySelector("#json").setAttribute("checked", "");
        }

        //请求参数的值
        document.querySelector("#parameter").value = result.parameter_body;

        //断言的类型
        if (result.assert_type == 1) {
            document.querySelector("#contains").setAttribute("checked", "");
        }
        else if (result.assert_type == 2) {
            document.querySelector("#mathches").setAttribute("checked", "");
        }

        //断言的值
        document.querySelector("#assert").value = result.assert_text;

        //用例的名称
        document.querySelector("#case_name").value = result.name;

        // 初始化菜单
        SelectInit(result.project_id, result.module_id);

    });

}