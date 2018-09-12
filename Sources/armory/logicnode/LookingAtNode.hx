package armory.logicnode;

import iron.math.Vec4;
import iron.math.Quat;
import iron.object.Object;
import armory.trait.physics.RigidBody;

 
class LookingAtNode extends LogicNode {
	
	public function new(tree:LogicTree) {
		super(tree);
	}
	
	private inline function subvecs(a:Vec4, b:Vec4):Vec4 {
		return new Vec4(a.x-b.x, a.y-b.y, a.z-b.z, 1);
	}
	
	private inline function dotvecs(a:Vec4, b:Vec4):Float {
		return new Vec4().setFrom(a).dot(b);
	}
	
	private inline function normalize(v:Vec4):Vec4 {
		return new Vec4().setFrom(v).normalize();
	}
	
	private inline function crossvecs(a:Vec4, b:Vec4): Vec4 {
		return new Vec4().setFrom(a).cross(b);
	}
	
	private inline function multvec(v:Vec4, f:Float):Vec4 {
		return new Vec4().setFrom(v).mult(f);
	}
	
	override function run() {
		
		// read inputs
		var objFrom:Object = inputs[1].get();
		var objTo:Object = inputs[2].get();
		
		// face and main axis MUST be different
		var face:Vec4 = inputs[3].get().normalize();
		var mainAxis:Vec4 = inputs[4].get().normalize();
		
		// rotate around main axis
		
			// 1st
			// use mainAxis as normal of a thought plane
			// get the distance vector of objFrom and the objTo
			// project the distance vector into that plane
			
			// 2nd
			// also project the face vector into said plane and normalize the projected vector
		
			// 3rd
			// to get the sign of the angle: project the distance vector into the plane of the face vector and dot it with the cross of the main axis and the face.
			// calculate the angle between the two normalized vectors
		
			//4th
			// reset the rotation of objFrom and rotate around the main axis by said angle
		
		// 1st
		var dist:Vec4 = subvecs(objFrom.transform.world.getLoc(), objTo.transform.world.getLoc());
		var projDistance:Vec4 = normalize(subvecs(dist, multvec(mainAxis, dotvecs(mainAxis, dist))));
		
		trace(projDistance);
		// 2nd
		var projFace:Vec4 = normalize(subvecs(face, multvec(mainAxis, dotvecs(mainAxis, face))));
		
		// 3rd
		var tmpV:Vec4 = subvecs(dist, multvec(face, dotvecs(face, dist)));
		var tmpF:Float = dotvecs(tmpV, crossvecs(mainAxis, face));
		var mainAngle:Float = Math.acos(projDistance.dot(projFace));
		if(tmpF < 0)
			mainAngle = -mainAngle;
		
		//var mainAngle:Float = Math.asin(projDistance.cross(projFace).length());
		// 4th
		objFrom.transform.setRotation(0, 0, 0);
		objFrom.transform.rotate(mainAxis, mainAngle);
		
		// secondary rotation
			// 1st
			// normalize the main axis and the difference vector
			// calculate the angle between them
		
			// 2nd
			// rotate objFrom around the cross product of the normalized vectors by the new angle
		
		// 1st
		var distNorm:Vec4 = dist.normalize();
		var mainNorm:Vec4 = mainAxis.normalize();
		
		var secondaryAngle:Float = -Math.acos(distNorm.dot(mainNorm)) -Math.PI/2;
		
		//secondaryAngle = (iron.system.Time.time() % Math.PI) - Math.PI/2;
		//secondaryAngle = -Math.PI/2;
		trace(secondaryAngle);
		// 2nd
		objFrom.transform.rotate(normalize(crossvecs(distNorm,mainNorm)), secondaryAngle);
		
		objFrom.transform.buildMatrix();
		
		#if arm_physics
		var rigidBody = objFrom.getTrait(RigidBody);
		if (rigidBody != null) rigidBody.syncTransform();
		#end
	}
}
