package armory.logicnode;

import iron.object.Object;
import armory.system.Event;

class ReturnFunctionNode extends LogicNode {

	var name1:String;
	var t:Bool=false;
	var id:Int;

	var _property0:String;
	public var property0(get, set):String;
	var listener:TEvent = null;

	public function new(tree:LogicTree) {
		super(tree);
		tree.notifyOnRemove(onRemove);
	}

	function get_property0():String {
		return _property0;
	}

	function set_property0(s:String):String {
		listener = Event.add(s, onEvent, tree.object.uid);
		return _property0 = s;
	}

	function onEvent() {
		name1 = _property0;
		id = inputs[0].get();
		if (iron.Scene.global.properties == null) iron.Scene.global.properties = new Map();
		if (iron.Scene.global.properties.get(name1+"run")!=0) recieve();
	}

	function onRemove() {
		if (listener != null) Event.removeListener(listener);
	}

	override function get(from:Int):Dynamic {	
		t = false;
		for (i in 1...outputs.length){
			if (from==i) return iron.Scene.global.properties.get(name1+"ret"+id+i);						
		}
		return null;	
}
	function recieve(){
			if (iron.Scene.global.properties.get(name1+"end")==id){		
				t = true;
				runOutputs(0);
			}
		}
}