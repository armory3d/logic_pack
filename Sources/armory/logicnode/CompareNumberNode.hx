package armory.logicnode;

class CompareNumberNode extends LogicNode {
	
	public var property0:String;
	public var property1:Float;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function get(index:Int):Bool {
		var result:Bool = false;
		switch(property0) {
			case "EQUAL": {
				return inputs[0].get() == inputs[1].get();
			}
			case "ALMOST EQUAL": {
				return Math.abs(inputs[0].get() - inputs[1].get()) < property1;
			}
			case "LESS": {
				return inputs[0].get() < inputs[1].get();
			}
			case "MORE": {
				return inputs[0].get() > inputs[1].get();
			}
			case "LESS EQUAL": {
				return inputs[0].get() <= inputs[1].get();
			}
			case "MORE EQUAL": {
				return inputs[0].get() >= inputs[1].get();
			}
			default: {
				trace("This should not have happened. The NumberCompare Node ran into the default case and will thus always be false. Please report this error.");
				return false;
			}
		}
	}
} 
