# TaskSchedulerHeaps-PythonDSA
A structured prioritization engine designed for productivity platforms that schedules tasks dynamically using a binary Min-Heap.

By structuring heap entries with a unique auto-incrementing index sequence, the architecture eliminates raw object comparison collisions when multiple tasks share identical priority coefficients. Time windows are evaluated dynamically, matching workloads against distinct execution limits.

## Core Features
### Min-Heap Urgency Ordering
- Organizes task nodes directly by numerical priority value, ensuring that the highest priority job (lowest numerical index) stays instantly accessible at the root node.

### Deterministic Tie-Breaking
- Integrates an auto-incrementing insertion tracker sequence to resolve comparison logic order when multiple tasks fall under the exact same priority tier.

### Relative Deadline Filtering
- Simulates current timeline configurations and filters out invalid or expired tasks by comparing execution duration bounds against hard target deadlines.

### Dynamic Priority Recalibration
- Re-evaluates tree properties on the fly by cleanly isolating, mutating, and re-heapifying individual task items if urgency requirements shift post-insertion.
