
# Parameters

    Name :                      causal1_CFagent_convert3-0
    Main :                      CFagent
    Level :                     Levels.Causal1
    Hours :                     13.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
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
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Minutes used :              775 minutes.
    Hours used :                12 hours.

# Profiling


      23196762928 function calls (23008937461 primitive calls) in 46519.62 seconds

##    Ordered by: cumulative time
   List reduced from 484 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 46519.625 46519.625 {built-in method builtins.exec}
                      1    4.608    4.608 46519.625 46519.625 <string>:1(<module>)
                      1  146.452  146.452 46515.017 46515.017 main.py:96(CFagent)
                5958879   23.824    0.000 17851.539    0.003 agent.py:28(learn)
                5958879  442.289    0.000 14863.356    0.002 learner.py:42(Qlearn)
        210096734/22272958  869.931    0.000 7731.444    0.000 module.py:866(_call_impl)
               16314079   42.436    0.000 7258.873    0.000 network.py:24(forward)
               16314079  228.570    0.000 7113.788    0.000 container.py:117(forward)
                1986293  211.430    0.000 6891.377    0.003 agent.py:53(_learn)
                1986293  210.090    0.000 6387.234    0.003 agent.py:189(_learn)
                5958879   50.916    0.000 6257.122    0.001 optimizer.py:84(wrapper)
                5958879   26.053    0.000 6018.462    0.001 grad_mode.py:24(decorate_context)
                1986293    9.418    0.000 5945.593    0.003 game.py:36(step)
                5958879  176.847    0.000 5935.073    0.001 adam.py:55(step)
                5958879 1215.041    0.000 5565.872    0.001 _functional.py:53(adam)
                1986293   12.942    0.000 5530.110    0.003 layers.py:594(step)
                1986293 2853.445    0.001 5320.670    0.003 replaybuffer.py:28(teleporter_save_data)
                1986293   59.482    0.000 4535.376    0.002 agent.py:114(_learn)
                1986293  466.848    0.000 4353.334    0.002 agent.py:197(counterfact)
                5958879   25.183    0.000 3772.818    0.001 tensor.py:195(backward)
                5958879   22.704    0.000 3746.739    0.001 __init__.py:68(backward)
                5177157  139.762    0.000 3729.905    0.001 agent.py:48(__call__)
                1986293 2219.628    0.001 3640.311    0.002 agent.py:85(interveen)
                5958879 3592.262    0.001 3592.262    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1986293  174.851    0.000 3184.392    0.002 layers.py:18(step)
                1986293 2324.424    0.001 3040.882    0.002 replaybuffer.py:22(sample_data)
              198369524  237.321    0.000 2993.376    0.000 layer.py:82(move)
                1986293 1956.560    0.001 2585.129    0.001 replaybuffer.py:49(sample_data)
               32628158   70.047    0.000 2569.946    0.000 conv.py:398(forward)
               32628158   44.730    0.000 2465.388    0.000 conv.py:390(_conv_forward)
               32628158 2420.658    0.000 2420.658    0.000 {built-in method conv2d}
                1986294  211.077    0.000 2314.158    0.001 layers.py:565(update)
              172188232 2197.787    0.000 2197.787    0.000 {built-in method clone}
               44969651   91.973    0.000 2055.903    0.000 linear.py:93(forward)
               44969651   36.607    0.000 1918.157    0.000 functional.py:1737(linear)
               44969651 1872.009    0.000 1872.009    0.000 {built-in method torch._C._nn.linear}
               25151500 1821.311    0.000 1821.311    0.000 {built-in method tensor}
               19389311   13.697    0.000 1640.106    0.000 game.py:32(board)
                1205457   12.318    0.000 1566.308    0.001 agent.py:167(choose_action)
               23835522  903.452    0.000 1561.692    0.000 layer.py:143(NoRock_update)
                1986293  942.599    0.000 1553.602    0.001 agent.py:66(modify)
              198253796  222.599    0.000 1275.733    0.000 layers.py:605(isFree)
              198369524  310.367    0.000 1252.827    0.000 layers.py:611(check)
               29012673 1171.572    0.000 1171.572    0.000 {built-in method cat}
              111232408 1142.288    0.000 1142.288    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               61283730   47.988    0.000 1140.917    0.000 activation.py:713(forward)
               61283730   52.456    0.000 1092.929    0.000 functional.py:1364(leaky_relu)
             1079542347  903.256    0.000 1053.134    0.000 layer.py:79(isFree)
               61283730 1029.201    0.000 1029.201    0.000 {built-in method torch._C._nn.leaky_relu}
                7163450   47.566    0.000 1028.050    0.000 agent.py:58(modify_board)
                1986293   37.075    0.000 1002.568    0.001 agent.py:163(__call__)
              111232408  998.170    0.000  998.170    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1986293   35.920    0.000  947.502    0.000 agent.py:109(__call__)
                5958879  139.255    0.000  860.416    0.000 optimizer.py:189(zero_grad)
                2293510   20.769    0.000  695.413    0.000 layers.py:615(restart)
                7163450  655.757    0.000  655.757    0.000 {built-in method torch._C._nn.one_hot}
               55616204  618.729    0.000  618.729    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1986293   44.018    0.000  572.833    0.000 replaybuffer.py:18(stacker)
                1986293  229.260    0.000  551.919    0.000 replaybuffer.py:55(CF_save_data)
               55616204  547.829    0.000  547.829    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              181337975  541.740    0.000  541.740    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              198629400   55.983    0.000  532.934    0.000 {built-in method builtins.all}
                2293510   11.783    0.000  518.423    0.000 level.py:8(__init__)
               55616204  514.815    0.000  514.815    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               55616204  512.290    0.000  512.290    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              616784673  143.026    0.000  499.236    0.000 layers.py:571(<genexpr>)
                1986293   39.386    0.000  492.810    0.000 replaybuffer.py:45(stacker)
                2293510   28.130    0.000  429.070    0.000 levels.py:122(generate)
                1986293  245.438    0.000  406.265    0.000 collector.py:54(collect)
               55616204  393.014    0.000  393.014    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5177157  138.857    0.000  385.612    0.000 exploration.py:53(softmaxer)
              566734297  377.684    0.000  377.684    0.000 layer.py:122(elements)
                8943931   73.583    0.000  375.637    0.000 level.py:41(notUsed)
             1314097325  270.802    0.000  369.938    0.000 enum.py:646(__hash__)
              198369524  232.241    0.000  367.939    0.000 layers.py:143(check)
              198629400  229.698    0.000  337.720    0.000 layers.py:111(isDone)
              389313512  254.236    0.000  315.715    0.000 tensor.py:906(grad)
                5958879    7.815    0.000  285.218    0.000 loss.py:527(forward)
                5958879   22.375    0.000  277.404    0.000 functional.py:2898(mse_loss)
                3191750   16.880    0.000  273.906    0.000 exploration.py:47(epsilonGreedy)
                3972586  100.957    0.000  271.885    0.000 random.py:315(sample)
        3341767258/3341767255  231.596    0.000  269.645    0.000 {built-in method builtins.len}
              198369524  180.094    0.000  268.912    0.000 layers.py:47(check)
                5958880  262.395    0.000  262.395    0.000 {built-in method nonzero}
              198369524  167.825    0.000  260.551    0.000 layers.py:124(check)
               32628158   21.973    0.000  185.924    0.000 flatten.py:39(forward)
             2232239078  183.755    0.000  183.755    0.000 layer.py:75(positions)
                5958879  182.930    0.000  182.930    0.000 {built-in method torch._C._nn.mse_loss}
               11917758  171.418    0.000  171.418    0.000 {built-in method sum}
                5959714  165.121    0.000  165.121    0.000 {built-in method max}
               32628158  163.951    0.000  163.951    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              173820624  109.235    0.000  156.578    0.000 layer.py:102(remove)
               13761060   13.728    0.000  151.298    0.000 layer.py:56(restart)
                8943931    7.123    0.000  150.052    0.000 level.py:38(elementsIn)
              215275811  147.471    0.000  147.471    0.000 {built-in method torch._C._get_tracing_state}
              260295975  103.143    0.000  145.498    0.000 layer.py:106(add)
                7945172   12.071    0.000  145.414    0.000 tensor.py:525(__rsub__)
                1778515   65.140    0.000  140.235    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7945172  131.506    0.000  131.506    0.000 {built-in method rsub}
                5958879  128.858    0.000  128.858    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9493316: <causal1_CFagent_convert3_0> in cluster <dcc> Done

Job <causal1_CFagent_convert3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  2 22:10:08 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  2 22:10:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 22:10:09 2021
Terminated at Sat Apr  3 11:06:49 2021
Results reported at Sat Apr  3 11:06:49 2021

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

    CPU time :                                   46393.70 sec.
    Max Memory :                                 7021 MB
    Average Memory :                             5219.55 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9363.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   46603 sec.
    Turnaround time :                            46601 sec.

The output (if any) is above this job summary.

