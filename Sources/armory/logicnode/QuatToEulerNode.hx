package armory.logicnode;

import iron.math.Mat4;
import iron.math.Vec4;
import iron.math.Quat;

class QuatToEulerNode extends LogicNode {
	
	
	public function new(tree:LogicTree) {
		super(tree);
		
	}


	override function get(from:Int):Dynamic {		
		var x:Float = inputs[0].get();
		var y:Float = inputs[1].get();
		var z:Float = inputs[2].get();
		var w:Float = inputs[3].get(); 
		var q = new Quat();

		q.x=x;
		q.y=y;
		q.z=z;
		q.w=w;
	
		var v = new Vec4();
		v.setFrom(q.getEuler());
		return v;		
		}
	}

	
