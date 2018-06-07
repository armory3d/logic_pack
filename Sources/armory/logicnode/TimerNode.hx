package armory.logicnode;

class TimerNode extends LogicNode {
	
	var currentDuration:Float = 0.0;
	var duration:Float = 0.0;
	
	var repetitions:Int = 0;
	var totalRepetitions:Int = 0;
	
	var running:Bool = false;
	
	var pause:Bool = false;
	var paused:Bool = false;
	
	var stop:Bool = false;

	public function new(tree:LogicTree) {
		super(tree);
	}
	
	override function run() {
		pause = inputs[1].get();
		stop = inputs[2].get();
		if(!running && !(stop || pause || paused)) {
			duration = inputs[3].get();
			currentDuration = duration;
			repetitions = inputs[4].get();
			totalRepetitions = repetitions;
			running = true;
			tree.notifyOnUpdate(update);
		}
		if(!running && !(stop || pause) && paused) {
			paused = false;
			running = true;
		}
	}
	
	override function get(from:Int):Dynamic {
		if(from == 1) {
			return running;
		} else {
			if(from == 2) {
				return paused;
			} else {
				if(from == 3) {
					return currentDuration;
				} else {
					if(from == 4) {
						if(repetitions < 0) {
							return 0;
						} else {
							return (totalRepetitions - repetitions + 1 - currentDuration/duration)/(totalRepetitions+1);
						}
					} else {
						return totalRepetitions - repetitions;
					}
				}
			}
		}
	}
	
	function update() {
		pause = inputs[1].get();
		stop = inputs[2].get();
		
		if(running && !(stop || pause)) {
			currentDuration -= iron.system.Time.delta;
			if(currentDuration <= 0) {
				runOutputs(0);
				if(repetitions == 0) {
					tree.removeUpdate(update);
					running = false;
					currentDuration = 0.0;
					duration = 0.0;
					repetitions = 0;
					totalRepetitions = 0;
					paused = false;
				}
				if(repetitions > 0) {
					repetitions -= 1;
					currentDuration = duration;
				}
				if(repetitions < 0) {
					currentDuration = duration;
				}
			}
		}
		
		if(running && pause) {
			running = false;
			if(!stop && pause)
				paused = true;
		}
		
		if(paused && !pause) {
			running = true;
			paused = false;
		}
		
		if(stop) {
			running = false;
			currentDuration = 0.0;
			duration = 0.0;
			repetitions = 0;
			totalRepetitions = 0;
			paused = false;
			tree.removeUpdate(update);
		}
	}
}
