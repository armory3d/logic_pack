package armory.logicnode;

import iron.object.Object;
import iron.math.Vec4;
import iron.math.Quat;
import armory.trait.physics.RigidBody;

class CameraController extends LogicNode {

var f:Bool = true;
var e1:Vec4 = new Vec4();
var e2:Vec4 = new Vec4();

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run() {

		// player inputs

		var player:Object = inputs[1].get();

		// camera inputs

		var camera:Object = inputs[2].get();
		var cameraSpeed:Float = inputs[3].get();

		var invX:Bool = inputs[4].get();
		var invY:Bool = inputs[5].get();

		var horzMove:Float = inputs[6].get();
		var horzSpeed:Float = inputs[7].get();
		var horzRestr:Bool = inputs[8].get();
		var horzMin:Float = inputs[9].get();
		var horzMax:Float = inputs[10].get();

		var vertMove:Float = inputs[11].get();
		var vertSpeed:Float = inputs[12].get();
		var vertRestr:Bool = inputs[13].get();
		var vertMin:Float = inputs[14].get();
		var vertMax:Float = inputs[15].get();

		if(player == null || camera == null) return;

		if(invX) horzMove = -horzMove;
		if(invY) vertMove = -vertMove;

		e1.equals(player.transform.rot.getEuler());
		e2.equals(camera.transform.rot.getEuler());

		if(f) {
			f = false;
			e1.y = e1.y - player.transform.rot.getEuler().x;
			e1.z = e1.z - player.transform.rot.getEuler().y;
			e1.x = e1.x - player.transform.rot.getEuler().z;

			e2.y = e2.y - camera.transform.rot.getEuler().x;
			e2.z = e2.z - camera.transform.rot.getEuler().y;
			e2.x = e2.x - camera.transform.rot.getEuler().z;
		}

		e1.x = e1.x + horzMove * horzSpeed * cameraSpeed * iron.system.Time.delta;
		e2.y = e2.y + vertMove * vertSpeed * cameraSpeed * iron.system.Time.delta;

		if(horzRestr) {
			if(-e1.x <= horzMin)
				e1.x = -horzMin;
			if(-e1.x >= horzMax)
				e1.x = -horzMax;
		}

		var p1:Quat = player.transform.rot;
		var p2:Quat = new Quat().fromEuler(-e1.y, -e1.z, -e1.x);

		player.transform.rot = Quat.lerp(p1, p2, 0.5);
		player.transform.buildMatrix();

		if(vertRestr) {
			if(-e2.y <= vertMin)
				e2.y = -vertMin;
			if(-e2.y >= vertMax)
				e2.y = -vertMax;
		}

		var c1:Quat = camera.transform.rot;
		var c2:Quat = new Quat().fromEuler(-e2.y, -e2.z, -e2.x);

		camera.transform.rot = Quat.lerp(c1, c2, 0.5);
		camera.transform.buildMatrix();

		#if arm_physics
		var rigidBodyPlayer = player.getTrait(RigidBody);
		if (rigidBodyPlayer != null) rigidBodyPlayer.syncTransform();
		var rigidBodyCamera = camera.getTrait(RigidBody);
		if (rigidBodyCamera != null) rigidBodyCamera.syncTransform();
		#end

		if(horzMove != 0 || vertMove != 0)
			super.run();
	}
}
