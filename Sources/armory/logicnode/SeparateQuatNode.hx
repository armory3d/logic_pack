package armory.logicnode;

import iron.math.Mat4;
import iron.math.Vec4;
import iron.math.Quat;

class SeparateQuatNode extends LogicNode {


	public function new(tree:LogicTree) {
		super(tree);
		
	}


	override function get(from:Int):Dynamic {		
		var m:Mat4 = inputs[0].get();

		if (from == 0) return m.getQuat().x;
		else if (from == 1) return m.getQuat().y;
		else if (from == 2) return m.getQuat().z;
		else if (from == 3) return m.getQuat().w;
		else return m.getQuat().getEuler();
		
		}
	}

	
