
# Parameters

    Name :                      SuperLevel2_simple-2
    Main :                      simple
    Level :                     Levels.SuperLevel2
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.MiniBig
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      169878872440 function calls (169686493581 primitive calls) in 86117.51 seconds

##    Ordered by: cumulative time
   List reduced from 418 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.514 86117.514 {built-in method builtins.exec}
                      1    0.001    0.001 86117.514 86117.514 <string>:1(<module>)
                      1  141.047  141.047 86117.513 86117.513 main.py:67(simple)
                8015771   27.927    0.000 59224.172    0.007 game.py:42(step)
                8015771   37.715    0.000 57207.347    0.007 layers.py:827(step)
                8015771  707.772    0.000 40826.318    0.005 layers.py:17(step)
              801577100 2269.808    0.000 40044.224    0.000 layer.py:106(move)
              801577100 4696.437    0.000 29869.926    0.000 layers.py:844(check)
                8015771   26.924    0.000 20655.228    0.003 agent.py:29(learn)
                8015771  188.213    0.000 20609.613    0.003 agent.py:117(_learn)
                8015771  539.008    0.000 20421.400    0.003 learner.py:42(Qlearn)
                8015772 1165.930    0.000 16292.811    0.002 layers.py:793(update)
                8015771   50.646    0.000 8301.094    0.001 grad_mode.py:23(decorate_context)
        216425817/24047313  845.468    0.000 8180.329    0.000 module.py:715(_call_impl)
                8015771  282.687    0.000 8158.913    0.001 adam.py:55(step)
               16031542   38.842    0.000 7559.103    0.000 network.py:28(forward)
               16031542  202.890    0.000 7418.777    0.000 container.py:115(forward)
                8015771 1478.329    0.000 6660.490    0.001 functional.py:53(adam)
              801577100 1510.419    0.000 6573.839    0.000 layers.py:838(isFree)
              801577100 4501.586    0.000 6298.353    0.000 layers.py:471(check)
            22674461488 4115.231    0.000 5918.185    0.000 enum.py:646(__hash__)
               88173492 3252.383    0.000 5542.116    0.000 layer.py:159(update)
             6692207893 3934.049    0.000 5063.420    0.000 layer.py:103(isFree)
             1542207687 1180.373    0.000 4783.087    0.000 {built-in method builtins.any}
                8015771   46.951    0.000 4573.265    0.001 tensor.py:181(backward)
                8015771   28.577    0.000 4526.315    0.001 __init__.py:68(backward)
                8015771 4314.627    0.001 4314.627    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              801577100 3027.936    0.000 4259.391    0.000 layers.py:77(check)
                8015771   94.757    0.000 4232.806    0.001 agent.py:112(__call__)
              801577100 2303.228    0.000 4000.451    0.000 layers.py:246(check)
              801577100 2107.835    0.000 3810.884    0.000 layers.py:286(check)
             9464701584 2604.074    0.000 3199.870    0.000 layers.py:809(<genexpr>)
               34001451 2943.424    0.000 2943.424    0.000 {built-in method tensor}
               32063084   56.061    0.000 2648.852    0.000 conv.py:422(forward)
              801577200  253.504    0.000 2618.627    0.000 {built-in method builtins.all}
               32063084   65.508    0.000 2567.620    0.000 conv.py:414(_conv_forward)
               12852068  130.773    0.000 2529.697    0.000 layers.py:849(restart)
            26114887798 2524.389    0.000 2524.389    0.000 layer.py:99(positions)
               32063084 2490.149    0.000 2490.149    0.000 {built-in method conv2d}
               48094626  109.865    0.000 2485.777    0.000 linear.py:92(forward)
             2661675640  712.545    0.000 2469.969    0.000 layers.py:799(<genexpr>)
               16031542   17.625    0.000 2419.118    0.000 game.py:38(board)
               48094626  182.768    0.000 2325.988    0.000 functional.py:1669(linear)
              561104000 1297.552    0.000 2177.015    0.000 tensor.py:933(grad)
                8015771  184.418    0.000 1887.604    0.000 optimizer.py:167(zero_grad)
            22674493637 1802.959    0.000 1802.959    0.000 {built-in method builtins.hash}
               48094626 1628.575    0.000 1628.575    0.000 {built-in method addmm}
              801471410  909.937    0.000 1387.048    0.000 layers.py:113(isDone)
              801577100  886.669    0.000 1382.061    0.000 layers.py:273(check)
              801577100  882.683    0.000 1373.895    0.000 layers.py:313(check)
              160315420 1354.227    0.000 1354.227    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2757722448 1307.741    0.000 1307.741    0.000 layer.py:154(elements)
              993624036  489.507    0.000 1276.106    0.000 random.py:285(choice)
               12852068   60.493    0.000 1203.149    0.000 level.py:8(__init__)
              801577100  823.930    0.000 1192.694    0.000 layers.py:62(check)
              141372748  164.812    0.000 1151.334    0.000 layer.py:77(restart)
              160315420 1127.406    0.000 1127.406    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              801577100  708.888    0.000 1083.112    0.000 layers.py:48(check)
              689356386  365.691    0.000 1079.113    0.000 overrides.py:1070(has_torch_function)
               64126168   57.255    0.000 1030.088    0.000 activation.py:713(forward)
               64126168   83.918    0.000  972.833    0.000 functional.py:1292(leaky_relu)
              801577100  617.174    0.000  907.639    0.000 layers.py:23(check)
               64126168  879.482    0.000  879.482    0.000 {built-in method torch._C._nn.leaky_relu}
             9729757515  783.454    0.000  783.454    0.000 {method 'random' of '_random.Random' objects}
        11308647776/11308647775  725.142    0.000  777.074    0.000 {built-in method builtins.len}
               80157710  757.257    0.000  757.257    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1292774527  535.224    0.000  720.560    0.000 layer.py:138(add)
               80157710  715.290    0.000  715.290    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              993624036  492.100    0.000  702.689    0.000 random.py:250(_randbelow_with_getrandbits)
                8015771  402.721    0.000  698.516    0.000 collector.py:46(collect)
               12852168  330.208    0.000  682.492    0.000 layers.py:36(reset)
               80157710  642.153    0.000  642.153    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               12852068  341.862    0.000  625.531    0.000 levels.py:368(generate)
             5504604467  614.719    0.000  614.719    0.000 layer.py:211(isBlocking)
               80157710  560.882    0.000  560.882    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             7887251320  537.010    0.000  537.010    0.000 layer.py:92(isDead)
               12852068  222.127    0.000  472.314    0.000 level.py:16(<dictcomp>)
               80157710  434.646    0.000  434.646    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              508799622  271.489    0.000  423.845    0.000 layer.py:134(remove)
                8015771   12.080    0.000  411.175    0.000 loss.py:445(forward)
                8015771   46.827    0.000  399.095    0.000 functional.py:2637(mse_loss)
             1426807398  320.497    0.000  397.315    0.000 overrides.py:1083(<genexpr>)
                8015771   30.628    0.000  358.754    0.000 exploration.py:47(epsilonGreedy)
             1603154200  339.787    0.000  339.787    0.000 {method 'union' of 'set' objects}
              801577200  251.561    0.000  331.728    0.000 layers.py:52(isDone)
             3875935577  304.254    0.000  304.254    0.000 {method 'append' of 'list' objects}
               48094626  297.243    0.000  297.243    0.000 {method 't' of 'torch._C._TensorBase' objects}
               88173492  288.447    0.000  288.447    0.000 layer.py:171(<listcomp>)
               88173492  266.624    0.000  266.624    0.000 layer.py:172(<listcomp>)
                8015771  243.511    0.000  243.511    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                8015771  230.458    0.000  230.458    0.000 {built-in method torch._C._nn.mse_loss}
               16031542  225.936    0.000  225.936    0.000 {built-in method sum}
               80157760   94.997    0.000  219.004    0.000 tensor.py:596(__hash__)
                8016572  205.127    0.000  205.127    0.000 {built-in method max}
                8015771   36.088    0.000  176.068    0.000 __init__.py:28(_make_grads)
               32063084   23.965    0.000  173.806    0.000 flatten.py:39(forward)
                8015771  171.683    0.000  171.683    0.000 {built-in method gather}
             1603154200  165.856    0.000  165.856    0.000 layer.py:86(check)
                8015771   37.504    0.000  158.228    0.000 tensor.py:506(__rsub__)
             1053878678  153.912    0.000  153.912    0.000 layer.py:190(grid)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578851: <SuperLevel2_simple_2> in cluster <dcc> Done

Job <SuperLevel2_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:07 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue May  4 07:07:06 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May  4 07:07:06 2021
Terminated at Wed May  5 07:02:35 2021
Results reported at Wed May  5 07:02:35 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85898.85 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2061.94 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86129 sec.
    Turnaround time :                            728308 sec.

The output (if any) is above this job summary.

