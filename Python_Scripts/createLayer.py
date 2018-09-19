    front_ip = cmds.imagePlane(
        name="front_IP",
        fileName="front_ref.jpg",
        lookThrough="front",
        showInAllViews=False)
    cmds.move(0,0,-950)
    cmds.createDisplayLayer(name="front_ref_L")


select -r front_IP1 ;
updateAnimLayerEditor("AnimLayerTab");
autoUpdateAttrEd;
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
dR_updateCommandPanel;
layerEditorCreateLayer 2;
createDisplayLayer -name "layer1" -number 1 -nr;
// Result: layer1 //
setFilterScript "initialShadingGroup";
// Result: 0 //
setFilterScript "initialParticleSE";
// Result: 0 //
setFilterScript "defaultLightSet";
// Result: 1 //
setFilterScript "defaultObjectSet";
// Result: 1 //
editMenuUpdate MayaWindow|mainEditMenu;
layerEditorDisplayLayerChange;
layerEditorDisplayLayerManagerChange;
layerEditorLayerButtonTypeChange layer1;
layerEditorLayerButtonTypeChange layer1;
