G.setIdleTimeOut(-1);
G.setOnSelectionOptions({unselected_transparent:false});

if (parent.window.location.search.indexOf('i=')>-1) {
    var list = parent.window.location.search.substring(parent.window.location.search.indexOf('i=')+2).split(',');
    var i=0;
    while(i<list.length){
        window.addVfbInd(list[i]);
        i++;
    }
}else{
    window.addVfbInd("VFB_00017894");
}
if (parent.window.location.search.indexOf('id=')>-1) {
    var info = ''
    if (parent.window.location.search.indexOf('&')>parent.window.location.search.indexOf('id=')) {
        info = parent.window.location.search.substring(parent.window.location.search.indexOf('id=')+3,parent.window.location.search.indexOf('&'));
    }else{
        info = parent.window.location.search.substring(parent.window.location.search.indexOf('id=')+3);
    }
    if (info.length > 0){
        Model.getDatasources()[0].fetchVariable(info, function(){ var instance = Instances.getInstance(info+'.'+info+'_meta'); setTermInfo(instance, instance.getParent().getId());});
    }
}
