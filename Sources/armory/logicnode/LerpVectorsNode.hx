package armory.logicnode;

import iron.math.Vec4;

class LerpVectorsNode extends LogicNode {

	var v = new Vec4();
	var v1:Vec4;
	var v2:Vec4;
	var t=0.0;
	var c:Float;
	var f=0.0;
	var abo:Bool;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run(from:Int) {
		v1 = inputs[1].get();
		v2 = inputs[2].get();
		t = inputs[3].get();
		
		f = (t / iron.system.Time.delta);		
	}

	override function get(from:Int):Dynamic {
		abo = inputs[4].get();
		// trace(t);	
		if (abo) {
			t = 0;
		}
		if (v1==null) {
			return null;
			c=1;
			}
		if (t>0) {					
			v.x=v1.x+((v2.x-v1.x)/f)*c;
			v.y=v1.y+((v2.y-v1.y)/f)*c;
			v.z=v1.z+((v2.z-v1.z)/f)*c;
			t -= iron.system.Time.delta;
			c++;
			return v;
		}
		else {c=1; return null;}
	}
}
