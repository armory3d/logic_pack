package armory.logicnode;

import iron.object.Object;
import iron.math.Vec4;
import armory.trait.physics.RigidBody;

class PlayerController extends LogicNode {

	var isCrouching:Bool;
	var lastKeyStateCrouch:Bool;

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

		var crouch:Bool = inputs[15].get();
		var crouchHold:Bool = inputs[16].get();
		var crouchMult:Float = inputs[17].get();

		if(player == null) return;
		if(isCrouching == null) isCrouching = false;
		if(lastKeyStateCrouch == null) lastKeyStateCrouch = false;
		var loc = new Vec4(0, 0, 0);

		// apply run Multiplier
		if(run) {
			fwSpeed *= runMult;
			lftSpeed *= runMult;
			rgtSpeed *= runMult;
			revSpeed *= runMult;
		}

		// Crouching logic
		if (crouchHold) {
			if(crouch) {	// directly set crouching parameter
				isCrouching = true;
			} else {
				isCrouching = false;
			}
		} else {
			if(lastKeyStateCrouch != crouch) {
				lastKeyStateCrouch = crouch;
				if(crouch) {	// toggle on every keypress
					isCrouching = !isCrouching;
				}
			}
		}

		// apply Crouch Multiplier
		if(isCrouching) {
			fwSpeed *= crouchMult;
			lftSpeed *= crouchMult;
			rgtSpeed *= crouchMult;
			revSpeed *= crouchMult;
		}

		// determine general movement
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

		// apply Movement
		player.transform.loc.add(vec);
		player.transform.buildMatrix();

		#if arm_physics
		var rigidBodyPlayer = player.getTrait(RigidBody);
		if (rigidBodyPlayer != null) rigidBodyPlayer.syncTransform();
		#end

		if(fw || lft || rgt || rev || jmp)
			super.run();
	}
}
