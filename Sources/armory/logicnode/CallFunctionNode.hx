package armory.logicnode;

import iron.object.Object;
import armory.system.Event;

class CallFunctionNode extends LogicNode {

	var n:String;
	var id:Int;
	var entries:Array<TEvent> = null;

	public function new(tree:LogicTree) {
		super(tree);
		tree.notifyOnUpdate(update);
	}

	function update(){
		n = inputs[1].get();
		id = inputs[2].get();
		if (iron.Scene.global.properties == null) iron.Scene.global.properties = new Map();
		if (iron.Scene.global.properties.get(n+"run")==id)iron.Scene.global.properties.set(n+"run",0);
	}

	override function run() {	
		n = inputs[1].get();
		id = inputs[2].get();
		iron.Scene.global.properties.set(n+"run",id);
		
		for(i in 2...inputs.length) {
			iron.Scene.global.properties.set(n+"var"+id+(i-2), inputs[i].get());
		}
		
		entries = Event.get(n);
		for (e in entries) e.onEvent();
		runOutputs(0);
	}
}