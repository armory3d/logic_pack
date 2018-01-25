package armory.logicnode;

class ArrayLoopIndiceNode extends LogicNode {

	var value:Dynamic;
	var index:Int;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run() {
		var ar:Array<Dynamic> = inputs[1].get();
		index = 0;
		for (val in ar) {
			value = val;
			index = index +1;

			runOutputs(0);
		}
		runOutputs(2);
	}

	
	override function get(from:Int):Dynamic {
		if (from == 1) return value;
		else if (from == 3) return index;
		else return index;
		
	}

	
}