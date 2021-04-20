
# Parameters

    Name :                      Diamonds3_0.5_var-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      37204591897 function calls (33505046354 primitive calls) in 35708.91 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.910 35708.910 {built-in method builtins.exec}
                      1    0.001    0.001 35708.910 35708.910 <string>:1(<module>)
                      1  130.314  130.314 35708.908 35708.908 allGraphsTrain.py:10(graphTrain)
                 576046 4879.650    0.008 11844.415    0.021 allGraphs.py:146(transformNot)
                 576046  531.705    0.001 8138.880    0.014 allGraphsTrain.py:35(<listcomp>)
              691260308 7774.364    0.000 7774.364    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 576046   13.311    0.000 7670.638    0.013 allGraphsTrain.py:29(<listcomp>)
               58180747 1741.379    0.000 7657.383    0.000 allGraphs.py:110(states)
               12540514   20.156    0.000 7607.174    0.001 allGraphs.py:158(getInterventions)
               11721583   10.036    0.000 6284.292    0.001 allGraphs.py:129(rightIntervention)
        662599080/11721583  343.577    0.000 6227.864    0.001 {built-in method builtins.min}
               45386892   18.079    0.000 6206.123    0.000 allGraphs.py:130(<lambda>)
        1313476577/45386892 1825.992    0.000 6188.044    0.000 allGraphs.py:74(expected_moves)
        1918967182/149910124  517.865    0.000 5914.378    0.000 allGraphs.py:78(<genexpr>)
              633651100 5624.893    0.000 5624.893    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 576046    1.989    0.000 2907.202    0.005 game.py:41(step)
                 576046    2.500    0.000 2787.681    0.005 layers.py:718(step)
             9286573288 1382.503    0.000 1992.182    0.000 enum.py:646(__hash__)
              663418011  348.093    0.000 1931.921    0.000 allGraphs.py:83(layers_not_in)
                 576047   75.463    0.000 1713.102    0.003 layers.py:684(update)
               17873215 1601.349    0.000 1601.349    0.000 {built-in method tensor}
              663418011  758.860    0.000 1583.828    0.000 allGraphs.py:84(<listcomp>)
                 576046   99.667    0.000 1542.422    0.003 allGraphsTrain.py:37(<listcomp>)
               15420745    8.303    0.000 1526.854    0.000 game.py:37(board)
               12540514   53.333    0.000 1289.850    0.000 allGraphs.py:153(format)
                 576046    2.035    0.000 1180.492    0.002 agent.py:29(learn)
                 576046   11.415    0.000 1177.284    0.002 agent.py:117(_learn)
                 576046   34.434    0.000 1165.869    0.002 learner.py:42(Qlearn)
                 576046   39.439    0.000 1069.116    0.002 layers.py:17(step)
               57604600   83.500    0.000 1024.627    0.000 layer.py:98(move)
               61060876  130.597    0.000  931.365    0.000 tensor.py:21(wrapped)
                2170949   16.687    0.000  915.185    0.000 layers.py:740(restart)
                 576046   40.184    0.000  882.337    0.002 allGraphsTrain.py:44(<listcomp>)
             1313476577  601.227    0.000  879.942    0.000 allGraphs.py:45(p)
                2170949    7.561    0.000  756.451    0.000 level.py:8(__init__)
                2170949   26.539    0.000  677.055    0.000 levels.py:288(generate)
               60484830  637.858    0.000  637.858    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               13024775  112.846    0.000  621.768    0.000 level.py:41(notUsed)
             9286575205  609.680    0.000  609.680    0.000 {built-in method builtins.hash}
               57604600  609.356    0.000  609.356    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               57604600  131.353    0.000  545.138    0.000 layers.py:735(check)
                 576046  297.105    0.001  535.030    0.001 agent.py:67(modify)
        13249058/1728138   48.400    0.000  466.256    0.000 module.py:715(_call_impl)
                 576046    3.153    0.000  461.568    0.001 grad_mode.py:23(decorate_context)
                 576046   15.570    0.000  452.145    0.001 adam.py:55(step)
                1152092    2.732    0.000  426.701    0.000 network.py:27(forward)
                1152092   10.764    0.000  417.487    0.000 container.py:115(forward)
                 576046   82.810    0.000  370.958    0.001 functional.py:53(adam)
               57604600   89.227    0.000  314.820    0.000 layers.py:729(isFree)
              159122166   86.946    0.000  308.330    0.000 {built-in method builtins.any}
               13024775    8.547    0.000  289.585    0.000 level.py:38(elementsIn)
                4608376  159.863    0.000  278.334    0.000 layer.py:167(NoRock_update)
                 576046    2.838    0.000  271.664    0.000 tensor.py:181(backward)
                 576046    1.989    0.000  268.826    0.000 __init__.py:68(backward)
              118665576   41.793    0.000  256.587    0.000 {built-in method builtins.all}
                 576046  254.554    0.000  254.554    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 576046    6.929    0.000  248.165    0.000 agent.py:112(__call__)
              445101998  176.659    0.000  225.592    0.000 layer.py:95(isFree)
             1316023646  211.630    0.000  216.173    0.000 {built-in method builtins.max}
              232932165   60.182    0.000  200.299    0.000 layers.py:690(<genexpr>)
                1728138    6.191    0.000  188.044    0.000 tensor.py:576(__iter__)
               59908784  187.750    0.000  187.750    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               13024775   89.457    0.000  187.272    0.000 level.py:39(<listcomp>)
                1728138  177.680    0.000  177.680    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2304184    3.769    0.000  166.623    0.000 conv.py:422(forward)
                2304184    4.249    0.000  161.435    0.000 conv.py:414(_conv_forward)
              498903759  131.488    0.000  159.266    0.000 layers.py:700(<genexpr>)
              100232138   47.850    0.000  156.648    0.000 overrides.py:1070(has_torch_function)
                2304184  156.334    0.000  156.334    0.000 {built-in method conv2d}
               17367592   12.271    0.000  136.653    0.000 layer.py:69(restart)
              617811272  131.274    0.000  131.274    0.000 level.py:32(inverse)
                2304184    4.964    0.000  123.037    0.000 linear.py:92(forward)
               28799117   70.805    0.000  117.416    0.000 layers.py:424(check)
               32258630   70.174    0.000  116.974    0.000 tensor.py:933(grad)
                2304184    8.699    0.000  115.790    0.000 functional.py:1669(linear)
                2171049   52.857    0.000  105.209    0.000 layers.py:36(reset)
                 576046    9.817    0.000  101.895    0.000 optimizer.py:167(zero_grad)
               57604700   59.894    0.000   96.050    0.000 layers.py:442(isDone)
               13024775   58.788    0.000   93.766    0.000 {built-in method _functools.reduce}
              547047593   92.159    0.000   92.159    0.000 enum.py:352(<genexpr>)
                 576046    4.126    0.000   84.655    0.000 agent.py:59(modify_board)
                2304184   82.723    0.000   82.723    0.000 {built-in method addmm}
                 576046   47.248    0.000   81.069    0.000 collector.py:46(collect)
               28806589   49.069    0.000   79.025    0.000 layers.py:437(check)
              861762488   78.853    0.000   78.853    0.000 layer.py:91(positions)
               28807435   47.198    0.000   77.597    0.000 layers.py:452(check)
                9216736   74.293    0.000   74.293    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              277199208   70.416    0.000   70.416    0.000 layer.py:146(elements)
              134858009   49.035    0.000   67.321    0.000 layer.py:130(add)
                2170949   34.469    0.000   66.608    0.000 level.py:16(<dictcomp>)
                9216736   62.107    0.000   62.107    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              263829336   51.994    0.000   61.759    0.000 overrides.py:1083(<genexpr>)
                 576046   39.200    0.000   58.719    0.000 allGraphsTrain.py:43(<listcomp>)
                3456276    2.896    0.000   55.857    0.000 activation.py:713(forward)
                 576046   55.774    0.000   55.774    0.000 {built-in method torch._C._nn.one_hot}
                3456276    4.873    0.000   52.961    0.000 functional.py:1292(leaky_relu)
                3456276   47.643    0.000   47.643    0.000 {built-in method torch._C._nn.leaky_relu}
                 576046   12.089    0.000   43.936    0.000 allGraphs.py:137(transform)
                4608368   43.551    0.000   43.551    0.000 {method 'add' of 'torch._C._TensorBase' objects}
        553920471/553920469   34.092    0.000   42.978    0.000 {built-in method builtins.len}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532015: <Diamonds3_0.5_var_0> in cluster <dcc> Done

Job <Diamonds3_0.5_var_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:42 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 19:10:09 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 19:10:09 2021
Terminated at Mon Apr 19 05:05:28 2021
Results reported at Mon Apr 19 05:05:28 2021

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

    CPU time :                                   35619.40 sec.
    Max Memory :                                 2060 MB
    Average Memory :                             2054.90 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14324.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35748 sec.
    Turnaround time :                            142606 sec.

The output (if any) is above this job summary.

