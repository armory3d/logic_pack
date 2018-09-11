package armory.logicnode;

import iron.math.Vec4;
import iron.math.Quat;

class SeparateQuatNode extends LogicNode {


	public function new(tree:LogicTree) {
		super(tree);
		
	}


	override function get(from:Int):Dynamic {		
		var q:Quat = inputs[0].get();

		if (from == 0) return q.x;
		else if (from == 1) return q.y;
		else if (from == 2) return q.z;
		else if (from == 3) return q.w;
		else return q.getEuler();
		
		}
	}

	
