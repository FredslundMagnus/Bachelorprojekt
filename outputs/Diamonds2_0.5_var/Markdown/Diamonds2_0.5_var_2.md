
# Parameters

    Name :                      Diamonds2_0.5_var-2
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.var
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      38131896767 function calls (33698103204 primitive calls) in 35704.88 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35704.882 35704.882 {built-in method builtins.exec}
                      1    0.001    0.001 35704.882 35704.882 <string>:1(<module>)
                      1   90.853   90.853 35704.882 35704.882 allGraphsTrain.py:10(graphTrain)
                 346811 5461.253    0.016 12201.534    0.035 allGraphs.py:146(transformNot)
                 346811  428.856    0.001 9806.111    0.028 allGraphsTrain.py:35(<listcomp>)
                6779756   13.965    0.000 9377.255    0.001 allGraphs.py:158(getInterventions)
                5808723    5.928    0.000 8528.745    0.001 allGraphs.py:129(rightIntervention)
        761072890/5808723  464.814    0.000 8493.797    0.001 {built-in method builtins.min}
               21447808   10.237    0.000 8480.189    0.000 allGraphs.py:130(<lambda>)
        1516337057/21447808 2489.599    0.000 8469.952    0.000 allGraphs.py:74(expected_moves)
        2250153416/73449872  704.857    0.000 8311.740    0.000 allGraphs.py:78(<genexpr>)
                 346811   10.160    0.000 7852.520    0.023 allGraphsTrain.py:29(<listcomp>)
               35028012 2062.141    0.000 7842.397    0.000 allGraphs.py:110(states)
              485538768 6713.427    0.000 6713.427    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              450854900 6189.183    0.000 6189.183    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              762043923  425.926    0.000 2664.542    0.000 allGraphs.py:83(layers_not_in)
            11326692812 1748.138    0.000 2543.837    0.000 enum.py:646(__hash__)
              762043923 1067.573    0.000 2238.616    0.000 allGraphs.py:84(<listcomp>)
                 346811    1.302    0.000 1685.636    0.005 game.py:41(step)
                 346811    1.725    0.000 1601.024    0.005 layers.py:718(step)
                 346811   97.922    0.000 1294.708    0.004 allGraphsTrain.py:37(<listcomp>)
             1516337057  750.676    0.000 1090.042    0.000 allGraphs.py:45(p)
               10002944 1043.620    0.000 1043.620    0.000 {built-in method tensor}
                8513812    5.369    0.000  982.282    0.000 game.py:37(board)
                 346811    1.122    0.000  970.238    0.003 agent.py:29(learn)
                 346811    7.434    0.000  968.336    0.003 agent.py:117(_learn)
                 346811   28.354    0.000  960.901    0.003 learner.py:42(Qlearn)
                 346812   47.626    0.000  844.836    0.002 layers.py:684(update)
                6779756   36.505    0.000  818.722    0.000 allGraphs.py:153(format)
               36761966   99.412    0.000  801.935    0.000 tensor.py:21(wrapped)
            11326693993  795.699    0.000  795.699    0.000 {built-in method builtins.hash}
                 346811   35.933    0.000  771.233    0.002 allGraphsTrain.py:44(<listcomp>)
                 346811   27.310    0.000  752.585    0.002 layers.py:17(step)
               34681100   56.568    0.000  722.153    0.000 layer.py:98(move)
               36415155  594.777    0.000  594.777    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               34681100  540.603    0.000  540.603    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 346811    2.040    0.000  409.741    0.001 grad_mode.py:23(decorate_context)
                 346811   11.079    0.000  403.751    0.001 adam.py:55(step)
                 346811  221.106    0.001  399.191    0.001 agent.py:67(modify)
               34681100   95.605    0.000  388.729    0.000 layers.py:735(check)
                 790990    7.421    0.000  378.079    0.000 layers.py:740(restart)
        7976653/1040433   32.513    0.000  349.290    0.000 module.py:715(_call_impl)
                 346811   73.744    0.000  347.872    0.001 functional.py:53(adam)
                 693622    1.901    0.000  320.048    0.000 network.py:27(forward)
                 790990    3.370    0.000  314.589    0.000 level.py:8(__init__)
                 693622    8.415    0.000  313.726    0.000 container.py:115(forward)
                 790990   11.859    0.000  284.976    0.000 levels.py:249(generate)
             1518348523  257.287    0.000  263.178    0.000 {built-in method builtins.max}
                5142094   46.386    0.000  260.494    0.000 level.py:41(notUsed)
               34681100   64.071    0.000  226.762    0.000 layers.py:729(isFree)
                 346811    1.970    0.000  216.154    0.001 tensor.py:181(backward)
                 346811    1.302    0.000  214.184    0.001 __init__.py:68(backward)
               96316325   58.166    0.000  207.011    0.000 {built-in method builtins.any}
                 346811  203.807    0.001  203.807    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 346811    4.623    0.000  186.223    0.001 agent.py:112(__call__)
               36068344  180.749    0.000  180.749    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3121308   98.014    0.000  175.729    0.000 layer.py:167(NoRock_update)
              308770516  121.533    0.000  162.691    0.000 layer.py:95(isFree)
                1387244    2.544    0.000  122.890    0.000 conv.py:422(forward)
                5142094    3.796    0.000  121.373    0.000 level.py:38(elementsIn)
                1040433    4.333    0.000  121.187    0.000 tensor.py:576(__iter__)
                1387244    2.966    0.000  119.406    0.000 conv.py:414(_conv_forward)
                1387244  115.882    0.000  115.882    0.000 {built-in method conv2d}
               71443166   28.505    0.000  115.594    0.000 {built-in method builtins.all}
                1040433  113.870    0.000  113.870    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              338902100   88.814    0.000  109.276    0.000 layers.py:700(<genexpr>)
               60345248   31.219    0.000  102.558    0.000 overrides.py:1070(has_torch_function)
                1387244    3.438    0.000   93.759    0.000 linear.py:92(forward)
                1387244    5.947    0.000   88.752    0.000 functional.py:1669(linear)
               19421470   52.675    0.000   83.756    0.000 tensor.py:933(grad)
                 346811    8.463    0.000   82.440    0.000 optimizer.py:167(zero_grad)
                5142094   38.282    0.000   78.416    0.000 level.py:39(<listcomp>)
              145839865   38.119    0.000   77.502    0.000 layers.py:690(<genexpr>)
                5548976   72.510    0.000   72.510    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 346811   42.072    0.000   70.558    0.000 collector.py:46(collect)
                1387244   63.942    0.000   63.942    0.000 {built-in method addmm}
                5548976   61.927    0.000   61.927    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 346811    2.755    0.000   60.996    0.000 agent.py:59(modify_board)
              242517183   56.730    0.000   56.730    0.000 level.py:32(inverse)
                7118910    5.356    0.000   53.728    0.000 layer.py:69(restart)
              521427565   53.615    0.000   53.615    0.000 layer.py:91(positions)
               17340913   32.121    0.000   52.097    0.000 layers.py:349(check)
               17343926   30.851    0.000   50.761    0.000 layers.py:337(check)
               17339899   29.754    0.000   49.467    0.000 layers.py:375(check)
               17340086   29.951    0.000   49.444    0.000 layers.py:387(check)
                2080866    1.885    0.000   44.611    0.000 activation.py:713(forward)
              129167325   43.819    0.000   43.819    0.000 layer.py:146(elements)
                2080866    3.145    0.000   42.726    0.000 functional.py:1292(leaky_relu)
                 791090   19.943    0.000   40.151    0.000 layers.py:36(reset)
                2774488   39.616    0.000   39.616    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              158839706   33.071    0.000   39.329    0.000 overrides.py:1083(<genexpr>)
                2080866   39.285    0.000   39.285    0.000 {built-in method torch._C._nn.leaky_relu}
                5142094   24.472    0.000   39.161    0.000 {built-in method _functools.reduce}
                 346811   38.541    0.000   38.541    0.000 {built-in method torch._C._nn.one_hot}
              213592589   37.472    0.000   37.472    0.000 enum.py:352(<genexpr>)
                 346811   25.109    0.000   37.349    0.000 allGraphsTrain.py:43(<listcomp>)
                2774488   36.313    0.000   36.313    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2774488   33.249    0.000   33.249    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              308770516   32.647    0.000   32.647    0.000 layer.py:203(isBlocking)
               61778690   23.678    0.000   32.341    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532014: <Diamonds2_0.5_var_2> in cluster <dcc> Done

Job <Diamonds2_0.5_var_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:41 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 11:31:13 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 11:31:13 2021
Terminated at Sun Apr 18 21:26:21 2021
Results reported at Sun Apr 18 21:26:21 2021

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
#BSUB -W 720
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35617.13 sec.
    Max Memory :                                 2083 MB
    Average Memory :                             2082.88 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14301.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35825 sec.
    Turnaround time :                            115060 sec.

The output (if any) is above this job summary.

