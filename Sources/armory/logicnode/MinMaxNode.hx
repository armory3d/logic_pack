package armory.logicnode;

class MinMaxNode extends LogicNode {

	var cond = false;
	var condmin = false;
	var condmax = false;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run(from:Int) {
		// Logic for this node
		var realvariable = inputs[1];
		var variable:Dynamic = inputs[1].get();
		var minimum:Dynamic = inputs[2].get();
		var maximum:Dynamic = inputs[3].get();

		condmin = minimum > variable;
		condmax = maximum < variable;
		
		if (condmin)
			realvariable.set(minimum);
			
		if (condmax)
			realvariable.set(maximum);

		runOutput(0);
	}
}
