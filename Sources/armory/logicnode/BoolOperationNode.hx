package armory.logicnode;

class BoolOperationNode extends LogicNode {
	
	public var property0:String;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function get(index:Int):Bool {
		var result:Bool = false;
		switch(property0) {
			case "AND": {
				result = true;
				for(i in 1...inputs.length) {
					if(!inputs[i].get()){
						result = false;
						break;
					}
				}
			}
			case "OR": {
				result = false;
				for(i in 1...inputs.length) {
					if(inputs[i].get()){
						result = true;
						break;
					}
				}
			}
			case "EQUAL": {
				result = inputs[1].get();
				if(inputs.length == 2) {
					result = true;
				} else {
					for(i in 2...inputs.length) {
						trace(i);
						if(inputs[i].get() != result) {
							result = false;
							break;
						}
					}
				}
			}
			case "XOR": {
				result = false;
				for(i in 1...inputs.length) {
					if(inputs[i].get()){
						result = !result;
					}
				}
			}
			default: {
				trace("This should not have happened. The BoolOperation Node ran into the default case and will thus always be false. Please report this error.");
				return false;
			}
		}
		inputs[0].get() ? return !result : return result;
	}
}