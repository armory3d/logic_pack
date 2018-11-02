package armory.logicnode;

import iron.object.Object;
import armory.system.Event;

class EndFunctionNode extends LogicNode {

	var name2:String;
	var id:Int;
	var entries:Array<TEvent> = null;

	public function new(tree:LogicTree) {
		super(tree);
		tree.notifyOnUpdate(update);
	}

	function update(){
		name2 = inputs[1].get();
		if (iron.Scene.global.properties == null) iron.Scene.global.properties = new Map();
		id = iron.Scene.global.properties.get(name2+"run");
		if (iron.Scene.global.properties.get(name2+"Rend")==id)iron.Scene.global.properties.set(name2+"Rend",0);
	}

	override function run(from:Int) {	
		id = iron.Scene.global.properties.get(name2+"run");
		if (iron.Scene.global.properties == null) iron.Scene.global.properties = new Map();
		for(i in 2...inputs.length) {
			iron.Scene.global.properties.set(name2+"Rret"+id+(i-1), inputs[i].get());
		}
		iron.Scene.global.properties.set(name2+"Rend",id);

		entries = Event.get(name2+"R");
		for (e in entries) e.onEvent();
		runOutput(0);
	}
}