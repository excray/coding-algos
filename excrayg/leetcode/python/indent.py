def uberPool(A, B, C, X, Y):
    initialDistance = abs(B[0]-A[0]) + abs(B[1]-A[1])
    
    if initialDistance == 0:
      return -1
    maxDist = 2*initialDistance
    distTillNow = abs(C[0]-A[0]) + abs(C[1]-A[1])
    distTillX = abs(C[0]-X[0]) + abs(C[1]-X[1])
    distTillY = abs(C[0]-Y[0]) + abs(C[1]-Y[1])
    distXToB = abs(X[0]-B[0]) + abs(X[1]-B[1])
    distYToB = abs(Y[0]-B[0]) + abs(Y[1]-B[1])
    
    finalX = distTillNow + distTillX + distXToB
    finalY = distTillNow + distTillY + distYToB
    
    if finalX <= maxDist and finalY <= maxDist:
      if distTillX < distTillY:
        return 1
      else:
        return 2
    elif finalX <= maxDist:
      return 1
    elif finalY <= maxDist:
      return 2
    else:
      return -1
      
