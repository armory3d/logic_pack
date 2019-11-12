package armory.logicnode;

import iron.math.Vec4;
import iron.object.Object;
import iron.object.Transform;

class LookingAtNode extends LogicNode {
	
	var transform:Transform = new Transform(new Object());

	var valid:Bool = false;

	var inView:Bool = true;

	public function new(tree:LogicTree) {
		super(tree);
		tree.notifyOnUpdate(update);
	}
	
	public function update() {
		valid = false;
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

	/**
	 * projects a vector into the (normal) plane of another vector. The plane is assumed to pass through the origin.
	 */
	private inline function project(v:Vec4, plane:Vec4) {
		return subvecs(v, multvec(plane, dotvecs(plane, v)));
	}

	public function compute() {

		// read inputs
		var fromVec:Vec4 = inputs[0].get();
		var toVec:Vec4 = inputs[1].get();
		
		// face and main axis MUST be different
		var face:Vec4 = inputs[2].get();
		var mainAxis:Vec4 = inputs[3].get();
		
		// disable rotations
		var disableMain:Bool = inputs[4].get();
		var disableSecondary:Bool = inputs[5].get();

		// restrict rotations
		var restrictMain:Bool = inputs[6].get();
		
		var restrictMainMin:Float = inputs[7].get();
		var restrictMainMax:Float = inputs[8].get();

		var restrictSecondary:Bool = inputs[9].get();

		var restrictSecondaryMin:Float = inputs[10].get();
		var restrictSecondaryMax:Float = inputs[11].get();

		var mainAngle:Float = 0;

		
		face = face.normalize();
		mainAxis = mainAxis.normalize();
		
		var dist:Vec4 = subvecs(toVec, fromVec);

		inView = true;

		if(!disableMain) {
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
			var projDistance:Vec4 = project(dist, mainAxis).normalize();

			// 2nd
			var projFace:Vec4 = project(face, mainAxis).normalize();

			// 3rd
			var tmpV:Vec4 = project(dist, face);
			var tmpF:Float = dotvecs(tmpV, crossvecs(mainAxis, face));
			mainAngle = Math.acos(projDistance.dot(projFace));
			if(tmpF < 0)
				mainAngle = -mainAngle;

			if(restrictMain) {
				if(mainAngle > restrictMainMax) {
					inView = false;
					mainAngle = restrictMainMax;
				}
				if(mainAngle < restrictMainMin) {
					inView = false;
					mainAngle = restrictMainMin;
				}
			}
			// trace(mainAngle);
		}
		
		// 4th
		transform.setRotation(0, 0, 0);
		transform.rotate(mainAxis, mainAngle);
		
		if(!disableSecondary) {
			// also rotate our face direction
			face.applyAxisAngle(mainAxis, mainAngle);

			// secondary rotation
			// 1st
			// our distance vector needs to be in the same plane as our new facing and our mainAxis vector. This plane is described by the cross product of these two vectors.
			// normalize the difference vector
			// calculate the angle between them

			// 2nd
			// rotate objFrom around the cross product of the normalized vectors by the new angle
		
			// 1st
			var projDistance:Vec4 = project(dist, crossvecs(mainAxis, face)).normalize();

			var secondaryAngle:Float = -Math.acos(projDistance.dot(mainAxis)) + Math.PI/2;
		
			if(restrictSecondary) {
				if(secondaryAngle > restrictSecondaryMax) {
					inView = false;
					secondaryAngle = restrictSecondaryMax;
				}
				if(secondaryAngle < restrictSecondaryMin) {
					inView = false;
					secondaryAngle = restrictSecondaryMin;
				}
			}

			// trace(secondaryAngle);
			// 2nd
			transform.rotate(crossvecs(projDistance,mainAxis).normalize(), secondaryAngle);
		}

		valid = true;
	}

	override function get(index:Int):Dynamic {
		if(!valid)
			compute();

		if(index == 0)
			return transform.rot.getEuler();
		else if(index == 1)
			return transform.rot;
		else
			return inView;
	}
}
