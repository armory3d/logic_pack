package armory.logicnode;

import iron.object.Object;
import iron.math.Vec4;
import iron.math.Quat;
import armory.trait.physics.RigidBody;

class FirstPersonController extends LogicNode {

var f:Bool = true;
var e1:Vec4 = new Vec4();
var e2:Vec4 = new Vec4();
var active:Bool = false;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run() {

		// player inputs

		var player:Object = inputs[1].get();
		var generalSpeed:Float = inputs[2].get();

		var fw:Bool = inputs[3].get();
		var fwSpeed:Float = inputs[4].get();

		var lft:Bool = inputs[5].get();
		var lftSpeed:Float = inputs[6].get();

		var rgt:Bool = inputs[7].get();
		var rgtSpeed:Float = inputs[8].get();

		var rev:Bool = inputs[9].get();
		var revSpeed:Float = inputs[10].get();

		var jmp:Bool = inputs[11].get();
		var hgt:Float = inputs[12].get();


		var run:Bool = inputs[13].get();
		var runMult:Float = inputs[14].get();

		// camera inputs

		var camera:Object = inputs[15].get();
		var cameraSpeed:Float = inputs[16].get();

		var invX:Bool = inputs[17].get();
		var invY:Bool = inputs[18].get();

		var horzMove:Float = inputs[19].get();
		var horzSpeed:Float = inputs[20].get();
		var horzRestr:Bool = inputs[21].get();
		var horzMin:Float = inputs[22].get();
		var horzMax:Float = inputs[23].get();

		var vertMove:Float = inputs[24].get();
		var vertSpeed:Float = inputs[25].get();
		var vertRestr:Bool = inputs[26].get();
		var vertMin:Float = inputs[27].get();
		var vertMax:Float = inputs[28].get();

		if(player == null || camera == null) return;

		var loc = new Vec4(0, 0, 0);

		if(run) {
			fwSpeed *= runMult;
			lftSpeed *= runMult;
			rgtSpeed *= runMult;
			revSpeed *= runMult;
		}
		if(fw) {
			var v = player.transform.world.look();
			v.x *= fwSpeed;
			v.y *= fwSpeed;
			v.z *= fwSpeed;
			loc.add(v);
		}
		if(lft) {
			var v = player.transform.world.right();
			v.x *= lftSpeed;
			v.y *= lftSpeed;
			v.z *= lftSpeed;
			loc.sub(v);
		}
		if(rgt) {
			var v = player.transform.world.right();
			v.x *= rgtSpeed;
			v.y *= rgtSpeed;
			v.z *= rgtSpeed;
			loc.add(v);
		}
		if(rev) {
			var v = player.transform.world.look();
			v.x *= revSpeed;
			v.y *= revSpeed;
			v.z *= revSpeed;
			loc.sub(v);
		}
		if(jmp) {
			var v = player.transform.world.up();
			v.x *= hgt;
			v.y *= hgt;
			v.z *= hgt;
			loc.add(v);
		}

		var vec = new Vec4(loc.x * generalSpeed, loc.y * generalSpeed, loc.z * generalSpeed);

		player.transform.loc.add(vec);
		player.transform.buildMatrix();

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

		if(fw || lft || rgt || rev || jmp || horzMove != 0 || vertMove != 0)
			super.run();
	}
}
