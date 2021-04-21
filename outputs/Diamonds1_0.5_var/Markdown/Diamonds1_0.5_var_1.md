
# Parameters

    Name :                      Diamonds1_0.5_var-1
    Main :                      graphTrain
    Level :                     Levels.Causal2
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


      19797853798 function calls (19022575865 primitive calls) in 35709.83 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.828 35709.828 {built-in method builtins.exec}
                      1    0.001    0.001 35709.828 35709.828 <string>:1(<module>)
                      1  181.761  181.761 35709.827 35709.827 allGraphsTrain.py:10(graphTrain)
                 684681 5335.403    0.008 13180.019    0.019 allGraphs.py:146(transformNot)
              684686872 9081.023    0.000 9081.023    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 684681   17.280    0.000 8332.896    0.012 allGraphsTrain.py:29(<listcomp>)
               69152882 1880.025    0.000 8315.661    0.000 allGraphs.py:110(states)
              616213300 5952.819    0.000 5952.819    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 684681  753.798    0.001 3940.772    0.006 allGraphsTrain.py:35(<listcomp>)
                 684681    2.601    0.000 3503.574    0.005 game.py:41(step)
                 684681    4.068    0.000 3357.819    0.005 layers.py:718(step)
               15603534   25.912    0.000 3186.974    0.000 allGraphs.py:158(getInterventions)
                 684682  102.057    0.000 2076.639    0.003 layers.py:684(update)
                 684681  126.399    0.000 2072.306    0.003 allGraphsTrain.py:37(<listcomp>)
               21936012 1862.094    0.000 1862.094    0.000 {built-in method tensor}
               19026940   10.218    0.000 1767.561    0.000 game.py:37(board)
               14593999   13.745    0.000 1644.303    0.000 allGraphs.py:129(rightIntervention)
        166872013/14593999  107.508    0.000 1574.992    0.000 {built-in method builtins.min}
               41646941   18.742    0.000 1550.939    0.000 allGraphs.py:130(<lambda>)
                 684681    2.703    0.000 1542.403    0.002 agent.py:29(learn)
                 684681   15.232    0.000 1538.168    0.002 agent.py:117(_learn)
        319150027/41646941  477.986    0.000 1532.198    0.000 allGraphs.py:74(expected_moves)
                 684681   45.327    0.000 1522.936    0.002 learner.py:42(Qlearn)
               15603534   67.188    0.000 1502.157    0.000 allGraphs.py:153(format)
        429781100/97978270  130.130    0.000 1289.860    0.000 allGraphs.py:78(<genexpr>)
                 684681   55.259    0.000 1272.643    0.002 layers.py:17(step)
               68468100  114.839    0.000 1210.535    0.000 layer.py:98(move)
               72576186  170.184    0.000 1187.343    0.000 tensor.py:21(wrapped)
                2868780   24.358    0.000 1131.133    0.000 layers.py:740(restart)
                 684681   54.116    0.000 1126.161    0.002 allGraphsTrain.py:44(<listcomp>)
                2868780   11.718    0.000  903.995    0.000 level.py:8(__init__)
               71891505  809.885    0.000  809.885    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               68468100  787.779    0.000  787.779    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2868780   33.080    0.000  786.188    0.000 levels.py:151(generate)
             3019842076  518.269    0.000  749.706    0.000 enum.py:646(__hash__)
               13770126  130.479    0.000  718.542    0.000 level.py:41(notUsed)
                 684681  394.853    0.001  710.147    0.001 agent.py:67(modify)
        15747663/2054043   66.002    0.000  616.389    0.000 module.py:715(_call_impl)
                 684681    4.624    0.000  594.646    0.001 grad_mode.py:23(decorate_context)
               68468100  148.431    0.000  586.870    0.000 layers.py:735(check)
                 684681   21.906    0.000  581.276    0.001 adam.py:55(step)
                1369362    3.764    0.000  559.176    0.000 network.py:27(forward)
                1369362   15.083    0.000  546.107    0.000 container.py:115(forward)
              167881548  101.151    0.000  488.755    0.000 allGraphs.py:83(layers_not_in)
                 684681  106.360    0.000  475.104    0.001 functional.py:53(adam)
               68468100   95.999    0.000  400.409    0.000 layers.py:729(isFree)
              167881548  192.376    0.000  387.605    0.000 allGraphs.py:84(<listcomp>)
                 684681    3.821    0.000  365.089    0.001 tensor.py:181(backward)
                 684681    2.821    0.000  361.268    0.001 __init__.py:68(backward)
              188842135  105.047    0.000  357.029    0.000 {built-in method builtins.any}
                4792774  206.021    0.000  348.083    0.000 layer.py:167(NoRock_update)
                 684681  342.194    0.000  342.194    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               13770126   10.662    0.000  336.217    0.000 level.py:38(elementsIn)
                 684681   10.207    0.000  335.896    0.000 agent.py:112(__call__)
              450379015  248.269    0.000  304.410    0.000 layer.py:95(isFree)
              141044386   54.786    0.000  291.025    0.000 {built-in method builtins.all}
                2054043    8.279    0.000  249.972    0.000 tensor.py:576(__iter__)
               71206824  244.984    0.000  244.984    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              319150027  162.089    0.000  236.963    0.000 allGraphs.py:45(p)
                2054043  236.366    0.000  236.366    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             3019844345  231.437    0.000  231.437    0.000 {built-in method builtins.hash}
              297865332   81.603    0.000  218.417    0.000 layers.py:690(<genexpr>)
               13770126  107.493    0.000  218.222    0.000 level.py:39(<listcomp>)
                2738724    5.439    0.000  218.100    0.000 conv.py:422(forward)
                2738724    6.482    0.000  210.566    0.000 conv.py:414(_conv_forward)
                2738724  203.019    0.000  203.019    0.000 {built-in method conv2d}
              119134628   62.524    0.000  201.082    0.000 overrides.py:1070(has_torch_function)
               20081460   16.438    0.000  195.731    0.000 layer.py:69(restart)
              524795360  139.262    0.000  172.744    0.000 layers.py:700(<genexpr>)
                2738724    6.709    0.000  160.145    0.000 linear.py:92(forward)
                2868880   75.424    0.000  151.809    0.000 layers.py:36(reset)
                2738724   11.577    0.000  150.393    0.000 functional.py:1669(linear)
               38342190   89.857    0.000  150.043    0.000 tensor.py:933(grad)
              661138315  146.227    0.000  146.227    0.000 level.py:32(inverse)
                 684681   12.309    0.000  129.256    0.000 optimizer.py:167(zero_grad)
               68468200   80.170    0.000  121.971    0.000 layers.py:113(isDone)
              599002109  115.959    0.000  115.959    0.000 enum.py:352(<genexpr>)
                 684681    5.576    0.000  113.635    0.000 agent.py:59(modify_board)
               13770126   67.314    0.000  107.333    0.000 {built-in method _functools.reduce}
                2738724  106.921    0.000  106.921    0.000 {built-in method addmm}
               34238100   64.605    0.000  103.860    0.000 layers.py:207(check)
               34242904   63.308    0.000  103.841    0.000 layers.py:231(check)
                 684681   59.895    0.000  103.014    0.000 collector.py:46(collect)
               34233399   62.921    0.000  102.441    0.000 layers.py:219(check)
                2868780   51.077    0.000   98.856    0.000 level.py:16(<dictcomp>)
               10954896   94.899    0.000   94.899    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              168262849   68.447    0.000   94.297    0.000 layer.py:130(add)
              921443674   94.146    0.000   94.146    0.000 layer.py:91(positions)
              343821650   87.741    0.000   87.741    0.000 layer.py:146(elements)
              313584166   66.662    0.000   78.737    0.000 overrides.py:1083(<genexpr>)
               10954896   78.181    0.000   78.181    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 684681   51.786    0.000   76.832    0.000 allGraphsTrain.py:43(<listcomp>)
                 684681   75.636    0.000   75.636    0.000 {built-in method torch._C._nn.one_hot}
                4108086    4.098    0.000   72.815    0.000 activation.py:713(forward)
              322213605   65.538    0.000   70.424    0.000 {built-in method builtins.max}
                4108086    6.991    0.000   68.717    0.000 functional.py:1292(leaky_relu)
                4108086   61.134    0.000   61.134    0.000 {built-in method torch._C._nn.leaky_relu}
                 684681   16.156    0.000   60.876    0.000 allGraphs.py:137(transform)
                5477448   55.254    0.000   55.254    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2054043   53.917    0.000   53.917    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532010: <Diamonds1_0.5_var_1> in cluster <dcc> Done

Job <Diamonds1_0.5_var_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:41 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 09:14:53 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 09:14:53 2021
Terminated at Sun Apr 18 19:10:07 2021
Results reported at Sun Apr 18 19:10:07 2021

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

    CPU time :                                   35619.83 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2058.97 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35715 sec.
    Turnaround time :                            106886 sec.

The output (if any) is above this job summary.

