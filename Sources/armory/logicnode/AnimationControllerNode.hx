package armory.logicnode;

import iron.object.Object;

class AnimationControllerNode extends LogicNode {

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run(from:Int) {
		var animated:Object = inputs[1].get();

		var idle:String = inputs[2].get();
		var blendTime:Float = inputs[3].get();

		if (animated == null) return;
		var animation = animated.animation;
		if (animation == null) animation = animated.getParentArmature(animated.name);

		var playAnimation:Bool = true;

		if(inputs.length > 4 && (inputs.length - 4) % 3 == 0) {
			for (index in 0...(cast((inputs.length-4)/3, Int))) {
				var active:Int = 3*index + 4;	// offset from default values
				var currentAnimation:Int = active + 1;	//offset from bool
				var currentBlendTime:Int = active + 2;	//offset from animation
				if(inputs[active].get() && playAnimation) {
					playAnimation = false;
					animation.play(inputs[currentAnimation].get(), function () {
						runOutput(1);
					}, inputs[currentBlendTime].get());
				}
			}
		}

		if(playAnimation) {
			animation.play(idle, function () {
				runOutput(1);
			}, blendTime);
		}

		runOutput(0);
	}
}
