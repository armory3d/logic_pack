package armory.logicnode;

class ToBool extends LogicNode {

	var value:Bool;
	var b=false;

	public function new(tree:LogicTree) {
		super(tree);
		
	}

	override function run(){
		b = true;
	}

	override function get(from:Int):Dynamic {		
		value = false;
		if (b){value = true;}
		b = false;
		return value;
		}
	}

	
