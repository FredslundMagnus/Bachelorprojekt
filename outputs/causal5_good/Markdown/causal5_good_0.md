
# Parameters

    Name :                      causal5_good-0
    Main :                      teleport
    Level :                     Levels.Causal5
    Hours :                     20.0
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
    Minutes used :              1197 minutes.
    Hours used :                19 hours.

# Profiling


      60727510777 function calls (60509875562 primitive calls) in 71877.57 seconds

##    Ordered by: cumulative time
   List reduced from 460 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 71877.571 71877.571 {built-in method builtins.exec}
                      1    2.002    2.002 71877.571 71877.571 <string>:1(<module>)
                      1  177.094  177.094 71875.568 71875.568 main.py:42(teleport)
                7773362   26.560    0.000 22506.719    0.003 agent.py:27(learn)
                7773362  529.265    0.000 18948.573    0.002 learner.py:42(Qlearn)
                3886681   16.697    0.000 17824.967    0.005 game.py:36(step)
                3886681   21.366    0.000 16927.978    0.004 layers.py:594(step)
                3886681  129.702    0.000 13609.578    0.004 agent.py:52(_learn)
                3886681 6519.711    0.002 11765.807    0.003 replaybuffer.py:28(teleporter_save_data)
                3886681  302.712    0.000 10607.122    0.003 layers.py:18(step)
              388668100  520.072    0.000 10268.208    0.000 layer.py:82(move)
        244839310/27205106  963.458    0.000 9356.871    0.000 module.py:715(_call_impl)
                3886681  110.260    0.000 8855.233    0.002 agent.py:113(_learn)
               19431744   48.887    0.000 8743.059    0.000 network.py:24(forward)
               19431744  227.104    0.000 8575.582    0.000 container.py:115(forward)
                3886681 5001.866    0.001 7867.383    0.002 agent.py:84(interveen)
                7773362   48.205    0.000 7615.229    0.001 grad_mode.py:23(decorate_context)
                7773362  249.094    0.000 7478.474    0.001 adam.py:55(step)
              388668100 1067.676    0.000 6552.456    0.000 layers.py:611(check)
                3886682  416.907    0.000 6271.520    0.002 layers.py:565(update)
                7773362 1390.724    0.000 6151.587    0.001 functional.py:53(adam)
                7771701  173.087    0.000 5775.472    0.001 agent.py:47(__call__)
                3886681 3359.647    0.001 5322.557    0.001 replaybuffer.py:22(sample_data)
                7773362   45.280    0.000 4440.823    0.001 tensor.py:181(backward)
                7773362   26.510    0.000 4395.543    0.001 __init__.py:68(backward)
                7773362 4185.578    0.001 4185.578    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              395064158 4156.136    0.000 4156.136    0.000 {built-in method clone}
                3886681 1552.656    0.000 3197.452    0.001 agent.py:65(modify)
               38863488   66.796    0.000 3164.945    0.000 conv.py:422(forward)
               38863488   80.768    0.000 3070.996    0.000 conv.py:414(_conv_forward)
               38863488 2976.021    0.000 2976.021    0.000 {built-in method conv2d}
               50521870  120.645    0.000 2742.459    0.000 linear.py:92(forward)
              388668100  703.694    0.000 2665.478    0.000 layers.py:605(isFree)
               50521870  194.387    0.000 2568.474    0.000 functional.py:1669(linear)
               34980138 1322.592    0.000 2325.443    0.000 layer.py:143(NoRock_update)
                5158387   55.308    0.000 2297.028    0.000 layers.py:615(restart)
               34978468 1963.492    0.000 1963.492    0.000 {built-in method cat}
             3387314956 1570.765    0.000 1961.784    0.000 layer.py:79(isFree)
              489721860 1167.821    0.000 1944.155    0.000 tensor.py:933(grad)
                5158387   26.458    0.000 1841.146    0.000 level.py:8(__init__)
                3886681   49.141    0.000 1828.684    0.000 agent.py:108(__call__)
               50521870 1811.272    0.000 1811.272    0.000 {built-in method addmm}
             6931344020 1270.144    0.000 1807.040    0.000 enum.py:646(__hash__)
               11658382   81.242    0.000 1730.501    0.000 agent.py:57(modify_board)
                7773362  160.933    0.000 1687.339    0.000 optimizer.py:167(zero_grad)
                3886681   73.745    0.000 1673.147    0.000 replaybuffer.py:18(stacker)
                5158387   82.034    0.000 1625.832    0.000 levels.py:247(generate)
               33529783  289.299    0.000 1457.764    0.000 level.py:41(notUsed)
               16658417 1283.180    0.000 1283.180    0.000 {built-in method tensor}
              139920516 1238.890    0.000 1238.890    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               69953614   58.670    0.000 1204.817    0.000 activation.py:713(forward)
              406722540 1164.484    0.000 1164.484    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               69953614   93.717    0.000 1146.147    0.000 functional.py:1292(leaky_relu)
               11658382 1107.509    0.000 1107.509    0.000 {built-in method torch._C._nn.one_hot}
              388668100  681.887    0.000 1104.101    0.000 layers.py:357(check)
              408103719  131.184    0.000 1100.674    0.000 {built-in method builtins.all}
              388668100  668.194    0.000 1083.005    0.000 layers.py:371(check)
              388668100  667.179    0.000 1076.663    0.000 layers.py:401(check)
              388668100  658.207    0.000 1067.285    0.000 layers.py:415(check)
               69953614 1043.371    0.000 1043.371    0.000 {built-in method torch._C._nn.leaky_relu}
              629638820  343.405    0.000 1038.726    0.000 overrides.py:1070(has_torch_function)
              139920516 1019.349    0.000 1019.349    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7773362    9.081    0.000 1016.473    0.000 game.py:32(board)
             1211193613  304.423    0.000 1002.682    0.000 layers.py:571(<genexpr>)
             8547753600  782.682    0.000  782.682    0.000 layer.py:75(positions)
               19435519  104.727    0.000  772.427    0.000 tensor.py:21(wrapped)
                3886681  420.713    0.000  722.341    0.000 collector.py:54(collect)
               69960258  713.667    0.000  713.667    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               69960258  670.983    0.000  670.983    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              695707415  268.017    0.000  663.828    0.000 {built-in method builtins.any}
              388668200  439.011    0.000  656.630    0.000 layers.py:111(isDone)
                7771701  221.345    0.000  596.226    0.000 exploration.py:53(softmaxer)
             1211716786  595.652    0.000  595.652    0.000 layer.py:122(elements)
               33529783   24.854    0.000  593.687    0.000 level.py:38(elementsIn)
               69960258  586.811    0.000  586.811    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              388668100  365.426    0.000  556.371    0.000 layers.py:344(check)
             6931372355  536.902    0.000  536.902    0.000 {built-in method builtins.hash}
               69960258  511.827    0.000  511.827    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              388668100  324.466    0.000  494.747    0.000 layers.py:388(check)
        4101449832/4101449830  285.265    0.000  395.960    0.000 {built-in method builtins.len}
                7773362   11.064    0.000  395.213    0.000 loss.py:445(forward)
             1581380095  392.934    0.000  392.934    0.000 level.py:32(inverse)
             1329234252  311.343    0.000  390.225    0.000 overrides.py:1083(<genexpr>)
               69960258  384.872    0.000  384.872    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               46425483   38.504    0.000  384.464    0.000 layer.py:56(restart)
                7773362   42.590    0.000  384.149    0.000 functional.py:2637(mse_loss)
               33529783  184.929    0.000  371.683    0.000 level.py:39(<listcomp>)
              573432224  251.435    0.000  348.690    0.000 layer.py:106(add)
               50521870  331.287    0.000  331.287    0.000 {method 't' of 'torch._C._TensorBase' objects}
             3387314956  324.313    0.000  324.313    0.000 layer.py:183(isBlocking)
              395457485  205.181    0.000  303.932    0.000 layer.py:102(remove)
               23320086  289.761    0.000  289.761    0.000 {built-in method sum}
                3886681  104.192    0.000  282.742    0.000 random.py:315(sample)
                5158487  139.590    0.000  278.910    0.000 layers.py:33(reset)
                3888235  267.910    0.000  267.910    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               11660043   54.448    0.000  246.440    0.000 tensor.py:506(__rsub__)
                3886735  240.089    0.000  240.091    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                7773362  223.941    0.000  223.941    0.000 {built-in method torch._C._nn.mse_loss}
               11660043  219.853    0.000  219.853    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               38863488   29.348    0.000  218.369    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9492737: <causal5_good_0> in cluster <dcc> Done

Job <causal5_good_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Fri Apr  2 14:23:06 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  2 14:23:08 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 14:23:08 2021
Terminated at Sat Apr  3 10:23:36 2021
Results reported at Sat Apr  3 10:23:36 2021

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

    CPU time :                                   71526.97 sec.
    Max Memory :                                 2809 MB
    Average Memory :                             2782.43 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13575.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   72135 sec.
    Turnaround time :                            72030 sec.

The output (if any) is above this job summary.

