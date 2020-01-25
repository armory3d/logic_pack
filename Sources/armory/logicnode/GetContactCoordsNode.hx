package armory.logicnode;

import iron.object.Object;
import armory.trait.physics.RigidBody;

class GetContactCoordsNode extends LogicNode {

	public function new(tree: LogicTree) {
		super(tree);
	}

	override function get(from: Int): Dynamic {
		var object: Object = inputs[0].get();
		if (object == null) return null;

#if arm_physics
	if (from == 0){
		var physics = armory.trait.physics.PhysicsWorld.active;
		var rbs = physics.getContacts(object.getTrait(RigidBody));
		var obs = [];
		if (rbs != null) for (rb in rbs) if (rb != null) obs.push(rb.object);
		return obs;
	}
	else if (from == 1){
		var physics = armory.trait.physics.PhysicsWorld.active;
		var cps = physics.getContactPairs(object.getTrait(RigidBody));
		var obs = [];
		if (cps != null) for (cp in cps) if (cp != null) obs.push(cp.posA);
		return obs;
	}
#end
		return null;
	}
}