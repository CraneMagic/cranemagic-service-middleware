def path_algorithm_easy(cranePosition, sourcePosition, targetPosition, craneMaxHeight=0):
    positions = []
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(cranePosition['xAxis']), '{:0>6d}'.format(cranePosition['yAxis']), '{:0>6d}'.format(cranePosition['zAxis']), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(cranePosition['xAxis']), '{:0>6d}'.format(cranePosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(sourcePosition['xAxis']), '{:0>6d}'.format(cranePosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(sourcePosition['xAxis']), '{:0>6d}'.format(sourcePosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(sourcePosition['xAxis']), '{:0>6d}'.format(sourcePosition['yAxis']), '{:0>6d}'.format(int(sourcePosition['zAxis'])), 'grab') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(sourcePosition['xAxis']), '{:0>6d}'.format(sourcePosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(targetPosition['xAxis']), '{:0>6d}'.format(sourcePosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(targetPosition['xAxis']), '{:0>6d}'.format(targetPosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(targetPosition['xAxis']), '{:0>6d}'.format(targetPosition['yAxis']), '{:0>6d}'.format(int(targetPosition['zAxis'])), 'release') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(targetPosition['xAxis']), '{:0>6d}'.format(targetPosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    return positions

def path_algorithm_two_point(cranePosition, targetPosition):
    print(cranePosition, targetPosition)
    targetPosition = {
        'xAxis': int(targetPosition['xAxis']),
        'yAxis': int(targetPosition['yAxis']),
        'zAxis': int(targetPosition['zAxis'])
    }
    positions = []
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(cranePosition['xAxis']), '{:0>6d}'.format(cranePosition['yAxis']), '{:0>6d}'.format(cranePosition['zAxis']), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(cranePosition['xAxis']), '{:0>6d}'.format(cranePosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(targetPosition['xAxis']), '{:0>6d}'.format(cranePosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(targetPosition['xAxis']), '{:0>6d}'.format(targetPosition['yAxis']), '{:0>6d}'.format(0), 'move') })
    positions.append({ 'Point': '%s,%s,%s,%s' % ('{:0>6d}'.format(targetPosition['xAxis']), '{:0>6d}'.format(targetPosition['yAxis']), '{:0>6d}'.format(int(targetPosition['zAxis'])), 'move') })
    return positions