package armory.logicnode;

import iron.object.Object;
import iron.math.Mat4;
import iron.math.Vec4;
import armory.trait.physics.RigidBody;

class LookNode extends LogicNode {

var e = new Vec4();
var f:Bool = true;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run(from:Int) {
		var LookX:Bool = inputs[3].get();
		var LookY:Bool = inputs[4].get();
		var Min:Float = inputs[5].get();
		var Max:Float = inputs[6].get();
		var object:Object = inputs[1].get();
		var vec:Vec4 = inputs[2].get();		

		e.equals(object.transform.rot.getEuler());

	if (f){
	e.y=e.y-object.transform.rot.getEuler().x;
	e.z=e.z-object.transform.rot.getEuler().y;
	e.x=e.x-object.transform.rot.getEuler().z;
	f=false;}

	if (LookX==true && LookY==true)
		{
			e.add(vec);
			}

	if (LookX==true && LookY==false)
		{e.y=e.y+vec.y;}

	if (LookX==false && LookY==true)
		{e.x=e.x+vec.x;}	

		
	if(Min!=0 && Max!= 0){
		if (-e.y<=Min)
			{e.y=-Min;}
		if (-e.y>=Max)
			{e.y=-Max;}	
	}
	object.transform.rot.fromEuler(-e.y, -e.z, -e.x);
	object.transform.buildMatrix();
		
		#if arm_physics
		var rigidBody = object.getTrait(RigidBody);
		if (rigidBody != null) rigidBody.syncTransform();
		#end

		runOutput(0);
		
	}			
}